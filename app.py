# -*- coding: utf-8 -*-
import traceback,json,decimal,time,datetime
from flask import Flask,render_template,request
from database import init_db, db_session
from models import *
from config import *

app = Flask(__name__)

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

@app.route('/')
def hello_world():
    return render_template('list.htm')

@app.route('/list', methods=["GET"])
def listPage():
    return render_template('list.htm')

@app.route('/rs', methods=["GET"])
def rsPage():
    return render_template('rs')

@app.route('/get/<roleId>')
def get(roleId):
    try:
        u = Members.query.filter(Members.roleId == roleId ).first()
    except Exception:
        return 'there isnot %s' % roleId
    return 'hello %s' % u.roleId


@app.route('/getAll')
def getAll():
    try:
        dataRangeStr = request.args.get('datarange_search')
        heroTypeStr = request.args.get('heroType_search')
        gameTypeStr = request.args.get('gameType_search')

        if dataRangeStr:
            dataRangeStart = dataRangeStr.split(' - ')[0]
            dataRangeEnd = dataRangeStr.split(' - ')[1]
            dataRangeStartTimeStamp  = int(time.mktime(time.strptime(dataRangeStart, '%Y-%m-%d %H:%M:%S')))
            dataRangeEndTimeStamp = int(time.mktime(time.strptime(dataRangeEnd, '%Y-%m-%d %H:%M:%S')))
        else:
            today = datetime.date.today()
            dataRangeStart = today - datetime.timedelta(days=29)
            dataRangeEnd = today + datetime.timedelta(days=1)
            dataRangeStartTimeStamp  = int(time.mktime(time.strptime(str(dataRangeStart), '%Y-%m-%d')))
            dataRangeEndTimeStamp = int(time.mktime(time.strptime(str(dataRangeEnd), '%Y-%m-%d')))-1

        sql = 'SELECT a.roleName 队员昵称,d.roleDesc 等级,COUNT(1) 总场次, SUM(IF(b.gameresult = 1,1,0)) 胜利场次 , SUM(IF(b.gameresult = 1,1,0))/COUNT(1) 胜率, \
            AVG(a.gradeGame) 平均得分,AVG(a.killCnt) 平均击杀,AVG(a.deadCnt) 平均死亡,AVG(a.assistCnt) 平均助攻, \
            AVG(a.totalHurtPercent) 平均总输出率,AVG(a.totalHurtHeroCntPercent) 平均对英雄输出率,AVG(a.totalBeHurtedCntPercent) 平均承伤率,AVG(a.joinGamePercent) 平均参团率, sum(b.mvpcnt)+sum(b.losemvp) MVP ,(sum(b.mvpcnt)+sum(b.losemvp))/COUNT(1) MVP率, \
            SUM(IF (a.heroPosition=0,1,0)) AS 上路,SUM(IF (a.heroPosition=1,1,0)) AS 中路,SUM(IF (a.heroPosition=2,1,0)) AS 下路,SUM(IF (a.heroPosition=3,1,0)) AS 打野,SUM(IF (a.heroPosition=4,1,0)) AS 辅助, \
            d.roleIcon 图标,d.sex 性别,d.rank 等级值 ,e.heroImg 英雄,e.useCnt 英雄使用次数,e.heroGrade 英雄平均得分,e.heroName 英雄名称,e.goldCnt 金牌数量,e.silverCnt 银牌数量,d.rankStar 星星数量 \
        FROM players AS a \
            LEFT JOIN matchs AS b \
                ON a.gameSeq = b.gameSeq \
                    AND a.gameSvrId = b.gameSvrId \
                    AND a.relaySvrId = b.relaySvrId \
            LEFT JOIN matchdetail AS c \
                ON a.gameSeq = c.gameSeq \
                    AND a.gameSvrId = c.gameSvrId \
                    AND a.relaySvrId = c.relaySvrId \
            LEFT JOIN members AS d \
                ON a.roleId=d.roleId \
            LEFT JOIN heroimage AS e \
                ON a.roleId=e.roleId \
        WHERE b.dteventtime >= :dataRangeStartTimeStamp and b.dteventtime<= :dataRangeEndTimeStamp and a.teamSide = 1 and a.heroPosition = :heroTypeStr and b.gametype = :gameTypeStr \
            AND d.roleId IS NOT NULL \
        GROUP BY a.roleId \
            ORDER BY 总场次 DESC,胜率 DESC,MAX(gradeLevelId) desc'

        if (not heroTypeStr) or int(heroTypeStr) == -1:
            sql = sql.replace('and a.heroPosition = :heroTypeStr','')

        if (not gameTypeStr) or int(gameTypeStr) == -1:
            sql = sql.replace('and b.gametype = :gameTypeStr', '')

        # print(sql)
        # print(gameTypeStr)
        rs = db_session.execute(sql,{'dataRangeStartTimeStamp':str(dataRangeStartTimeStamp),'dataRangeEndTimeStamp':str(dataRangeEndTimeStamp),'heroTypeStr':str(heroTypeStr),'gameTypeStr':str(gameTypeStr)})
        jsonStr = {"data":[]}
        for row in rs:
            tmpStr = []
            for num in range(0, 30):
                tmpStr.append(row[num])
            jsonStr["data"].append(tmpStr)
    except Exception:
        print('traceback.format_exc():\n%s' % traceback.format_exc())
    return json.dumps(jsonStr, cls=DecimalEncoder)


if __name__ == '__main__':
    app.run(
        host=serverIp,
        port=serverPort
    )
