# -*- coding: utf-8 -*-
import traceback,json,decimal,time,os
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

@app.route('/changeToken/<token>')
def changeToken(token):
    try:
        if token.isalnum():
            os.system(changeTokenPath+ ' ' + token)
        else:
            return 'Token Error!'
    except Exception:
        return 'Error!'
    return 'Done!'


@app.route('/getAll')
def getAll():
    try:
        my_session=db_session()
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
            dataRangeStart = today - datetime.timedelta(days=59)
            dataRangeEnd = today + datetime.timedelta(days=1)
            dataRangeStartTimeStamp  = int(time.mktime(time.strptime(str(dataRangeStart), '%Y-%m-%d')))
            dataRangeEndTimeStamp = int(time.mktime(time.strptime(str(dataRangeEnd), '%Y-%m-%d')))-1

        sql =  'SELECT a.roleName AS 队员昵称, d.roleDesc AS 等级, COUNT(1) AS 总场次 , SUM(IF(m.gameresult = 1, 1, 0)) AS 胜利场次 , SUM(IF(m.gameresult = 1, 1, 0)) / COUNT(1) AS 胜率 , AVG(a.gradeGame) AS 平均得分, AVG(a.killCnt) AS 平均击杀 , AVG(a.deadCnt) AS 平均死亡, AVG(a.assistCnt) AS 平均助攻 , AVG(a.totalHurtPercent) AS 平均总输出率, AVG(a.totalHurtHeroCntPercent) AS 平均对英雄输出率 , AVG(a.totalBeHurtedCntPercent) AS 平均承伤率, AVG(a.joinGamePercent) AS 平均参团率 , SUM(m.mvpcnt) + SUM(m.losemvp) AS MVP , (SUM(m.mvpcnt) + SUM(m.losemvp)) / COUNT(1) AS MVP率 , SUM(IF(a.heroPosition = 0, 1, 0)) AS 上路 , SUM(IF(a.heroPosition = 1, 1, 0)) AS 中路 , SUM(IF(a.heroPosition = 2, 1, 0)) AS 下路 , SUM(IF(a.heroPosition = 3, 1, 0)) AS 打野 , SUM(IF(a.heroPosition = 4, 1, 0)) AS 辅助 , d.roleIcon AS 图标, d.sex AS 性别, d.rank AS 等级值, e.heroImg AS 英雄, e.useCnt AS 英雄使用次数 , e.heroGrade AS 英雄平均得分, e.heroName AS 英雄名称, e.goldCnt AS 金牌数量, e.silverCnt AS 银牌数量, d.rankStar AS 星星数量 ' \
               'FROM members d LEFT JOIN heroimage e ON d.roleId = e.roleId ' \
               'LEFT JOIN ( SELECT `b`.`roleId` AS `roleId`, `b`.`dteventtime` AS `dteventtime`, `b`.`gametype` AS `gametype`, `b`.`wincamp` AS `wincamp`, `b`.`gametime` AS `gametime` , `b`.`killcnt` AS `killcnt`, `b`.`deadcnt` AS `deadcnt`, `b`.`assistcnt` AS `assistcnt`, `b`.`gameresult` AS `gameresult`, `b`.`mvpcnt` AS `mvpcnt` , `b`.`losemvp` AS `losemvp`, `b`.`heroId` AS `heroId`, `b`.`AcntCamp` AS `AcntCamp`, `b`.`mapName` AS `mapName`, `b`.`rampage` AS `rampage` , `b`.`gameSvrId` AS `gameSvrId`, `b`.`relaySvrId` AS `relaySvrId`, `b`.`gameSeq` AS `gameSeq`, `b`.`pvpType` AS `pvpType`, `b`.`multiCampRank` AS `multiCampRank` , `b`.`battleType` AS `battleType`, `b`.`branchEvaluate` AS `branchEvaluate`, `b`.`oldMasterMatchScore` AS `oldMasterMatchScore`, `b`.`newMasterMatchScore` AS `newMasterMatchScore`, `b`.`battleRoyaleEvaluate` AS `battleRoyaleEvaluate` , `b`.`desc` AS `desc`, `c`.`killCntOur` AS `killCntOur`, `c`.`killCntThey` AS `killCntThey`, `c`.`deadCntOur` AS `deadCntOur`, `c`.`deadCntThey` AS `deadCntThey` , `c`.`assistCntOur` AS `assistCntOur`, `c`.`assistCntThey` AS `assistCntThey`, `c`.`ldragonCntOur` AS `ldragonCntOur`, `c`.`ldragonCntThey` AS `ldragonCntThey`, `c`.`bdragonCntOur` AS `bdragonCntOur` , `c`.`bdragonCntThey` AS `bdragonCntThey`, `c`.`moneyOur` AS `moneyOur`, `c`.`moneyThey` AS `moneyThey`, `c`.`multiCampRankOur` AS `multiCampRankOur`, `c`.`multiCampRankThey` AS `multiCampRankThey` FROM matchs b LEFT JOIN matchdetail c ON (b.gameSeq = c.gameSeq AND b.gameSvrId = c.gameSvrId AND b.relaySvrId = c.relaySvrId) WHERE (b.dteventtime >= :dataRangeStartTimeStamp and b.dteventtime<= :dataRangeEndTimeStamp AND b.gametype = :gameTypeStr) ) m ON m.roleId = d.roleId ' \
               'LEFT JOIN players a ON (a.gameSeq = m.gameSeq AND a.gameSvrId = m.gameSvrId AND a.relaySvrId = m.relaySvrId) WHERE (a.roleName IS NOT NULL AND a.teamSide = 1 AND a.heroPosition = :heroTypeStr) GROUP BY a.roleId ORDER BY 总场次 DESC, 胜率 DESC, MAX(gradeLevelId) DESC'

        if (not heroTypeStr) or int(heroTypeStr) == -1:
            sql = sql.replace('AND a.heroPosition = :heroTypeStr','')

        if (not gameTypeStr) or int(gameTypeStr) == -1:
            sql = sql.replace('AND b.gametype = :gameTypeStr', '')

        # print(sql)
        # print(gameTypeStr)
        rs = my_session.execute(sql,{'dataRangeStartTimeStamp':str(dataRangeStartTimeStamp),'dataRangeEndTimeStamp':str(dataRangeEndTimeStamp),'heroTypeStr':str(heroTypeStr),'gameTypeStr':str(gameTypeStr)})
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
