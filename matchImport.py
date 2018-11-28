# -*- coding:utf-8 -*-

import http.client
import json
import traceback
import time

from database import init_db, db_session
from models import *
from config import *

def AddcRand(rStr):
    millis = str(round(time.time() * 1000))
    return rStr+"&cRand="+millis

# 创建matchs
def AddMatch(match):
    new_match = Matchs()
    new_match.dteventtime = match['dteventtime']
    new_match.gametype = match['gametype']
    new_match.wincamp = match['wincamp']
    new_match.gametime = match['gametime']
    new_match.killcnt = match['killcnt']
    new_match.deadcnt = match['deadcnt']
    new_match.assistcnt = match['assistcnt']
    new_match.gameresult = match['gameresult']
    new_match.mvpcnt = match['mvpcnt']
    new_match.losemvp = match['losemvp']
    new_match.heroId = match['heroId']
    new_match.AcntCamp = match['AcntCamp']
    new_match.mapName = match['mapName']
    # new_match.detailUrl = match['detailUrl']
    new_match.rampage = match['rampage']
    new_match.gameSvrId = match['gameSvrId']
    new_match.relaySvrId = match['relaySvrId']
    new_match.gameSeq = match['gameSeq']
    new_match.pvpType = match['pvpType']
    new_match.multiCampRank = match['multiCampRank']
    new_match.battleType = match['battleType']
    new_match.branchEvaluate = match['branchEvaluate']
    new_match.oldMasterMatchScore = match['oldMasterMatchScore']
    new_match.newMasterMatchScore = match['newMasterMatchScore']
    new_match.battleRoyaleEvaluate = match['battleRoyaleEvaluate']
    new_match.desc = match['desc']
    # new_match.heroIcon = match['heroIcon']
    return new_match


# 创建Players
def AddPlayer(newPlayer):
    player = Players()
    player.roleId=newPlayer['roleId']
    player.roleName=newPlayer['roleName']
    player.heroName=newPlayer['heroName']
    player.userId=newPlayer['userId']
    player.heroId=newPlayer['heroId']
    player.killCnt=newPlayer['killCnt']
    player.deadCnt=newPlayer['deadCnt']
    player.assistCnt=newPlayer['assistCnt']
    player.totalOutputPerMin=newPlayer['totalOutputPerMin']
    player.totalHurtHeroCntPerMin=newPlayer['totalHurtHeroCntPerMin']
    player.totalBeHurtedCntPerMin=newPlayer['totalBeHurtedCntPerMin']
    player.hero1TripleKillCnt=newPlayer['hero1TripleKillCnt']
    player.godLikeCnt=newPlayer['godLikeCnt']
    player.winMvp=newPlayer['winMvp']
    player.hero1UltraKillCnt=newPlayer['hero1UltraKillCnt']
    player.hero1RampageCnt=newPlayer['hero1RampageCnt']
    player.loseMvp=newPlayer['loseMvp']
    player.hero1GhostLevel=newPlayer['hero1GhostLevel']
    player.disGradeLevelId=newPlayer['disGradeLevelId']
    player.gradeLevelId=newPlayer['gradeLevelId']
    player.gradeLevel=newPlayer['gradeLevel']
    # player.finalEquipmentInfo=dict(newPlayer['finalEquipmentInfo'])
    player.maxKill=newPlayer['maxKill']
    player.maxHurt=newPlayer['maxHurt']
    player.maxAssist=newPlayer['maxAssist']
    player.maxTower=newPlayer['maxTower']
    player.maxBeHurt=newPlayer['maxBeHurt']
    player.heroSkillID=newPlayer['heroSkillID']
    player.heroSkillIcon=newPlayer['heroSkillIcon']
    player.heroIcon=newPlayer['heroIcon']
    player.gradeGame=newPlayer['gradeGame']
    player.totalHurtPercent=newPlayer['totalHurtPercent']
    player.totalHurtHeroCntPercent=newPlayer['totalHurtHeroCntPercent']
    player.totalBeHurtedCntPercent=newPlayer['totalBeHurtedCntPercent']
    player.acntcamp=newPlayer['acntcamp']
    player.playerId=newPlayer['playerId']
    player.gameScore=newPlayer['gameScore']
    player.branchEvaluate=newPlayer['branchEvaluate']
    player.heroPosition=newPlayer['heroPosition']
    player.usedtime=newPlayer['usedtime']
    player.newGrow=newPlayer['newGrow']
    player.newBattle=newPlayer['newBattle']
    player.newSurvive=newPlayer['newSurvive']
    player.newHurtHero=newPlayer['newHurtHero']
    player.newKDA=newPlayer['newKDA']
    player.maxMvpScore=newPlayer['maxMvpScore']
    player.totalWinNum=newPlayer['totalWinNum']
    player.totalLostNum=newPlayer['totalLostNum']
    player.avgMvpScore=newPlayer['avgMvpScore']
    player.isMI=newPlayer['isMI']
    player.oldMasterMatchScore=newPlayer['oldMasterMatchScore']
    player.newMasterMatchScore=newPlayer['newMasterMatchScore']
    player.defeatAcntRatio=newPlayer['defeatAcntRatio']
    player.joinGamePercent=newPlayer['joinGamePercent']
    player.sabcgrow=newPlayer['sabcgrow']
    player.sabcbattle=newPlayer['sabcbattle']
    player.sabcsurvive=newPlayer['sabcsurvive']
    player.sabchurtHero=newPlayer['sabchurtHero']
    player.sabcKDA=newPlayer['sabcKDA']
    player.battleRoyaleEvaluate=newPlayer['battleRoyaleEvaluate']
    player.battleRoyaleTotalTeamNum=newPlayer['battleRoyaleTotalTeamNum']
    player.battleRoyaleGrade=newPlayer['battleRoyaleGrade']
    player.battleRoyaleTimeToLive=newPlayer['battleRoyaleTimeToLive']
    player.battleRoyaleGrowValue=newPlayer['battleRoyaleGrowValue']
    # player.heroScoreGrade=dict(newPlayer['heroScoreGrade'])
    player.hornorPercent=newPlayer['hornorPercent']
    return player

try:

    conn = http.client.HTTPSConnection(requrl)
    conn.request('POST', reqMethodGameGroupmembers, AddcRand(reqGameGroupmembersPayload), headerdata)
    response = conn.getresponse()
    res = response.read()

    resData = json.loads(res.decode('utf-8'))
    teamMembers = resData['data']
    current_time = datetime.datetime.now()

    # 创建session对象:

    for member in teamMembers:
        print('============================================================ 开始保存队员信息 ============================================================')
        # print('成员数据')
        # print(member)
        roleId = member['roleId']


        # 创建新Member对象:
        new_member = Members()
        new_member.roleId = member['roleId']
        new_member.roleName = member['roleName']
        new_member.roleDesc = member['roleDesc']
        new_member.nickname = member['nickname']
        new_member.roleIcon = member['roleIcon']
        new_member.rank = 0
        new_member.updateDate = current_time
        try:

            new_member.sex = member['sex']
        except:
            new_member.sex = 0

        # 获取用户卡片
        try:
            reqGetRoleCardPayload = reqGetRoleCardPayload + "&roleid=" + new_member.roleId+"&friendUserId="+str(member['userId'])
            conn_card = http.client.HTTPSConnection(requrl)
            conn_card.request('POST', reqMethodGetRoleCard, AddcRand(reqGetRoleCardPayload), headerdata)
            response_card = conn_card.getresponse()
            res_card = response_card.read()

            resCardData = json.loads(res_card.decode('utf-8'))
            cardDate = resCardData['data']
            new_member.rankStar = int(cardDate['rankingStar'])
        except:
            print('出现异常：:\n%s' % traceback.format_exc())
            print('****** 获取用户卡片处理出错 ******')
            new_member.rankStar=0

        sessionMember = db_session()
        # 添加到session:
        sessionMember.merge(new_member)
        # 提交即保存到数据库:
        sessionMember.commit()
        print("队员：["+new_member.roleName+"] 资料保存完毕.......")



        if (isImport) :
            # print('请求参数')
            # print(AddcRand(reqPlayGetmatchlistPayload + '&roleId=' + roleId))

            try:
                conn.request('POST', reqMethodPlayGetmatchlist, AddcRand(reqPlayGetmatchlistPayload + '&roleId=' + roleId),
                             headerdata)
                matchListResponse = conn.getresponse()
                matchListRes = matchListResponse.read()
                matchListResData = json.loads(matchListRes.decode('utf-8'))
                matchList = matchListResData['data']['list']
                # print('比赛情况')
                # print(matchList)

                for match in matchList:
                    print('>> 开始保存队员的比赛信息')

                    gameSvrId = match['gameSvrId']
                    relaySvrId = match['relaySvrId']
                    gameSeq = match['gameSeq']

                    new_match = AddMatch(match)
                    new_match.roleId=roleId
                    if (new_match.gametype != '14' and new_match.gametype != '4' and new_match.gametype != '11'):
                        print('>> 只保存排位赛、巅峰赛、战队赛')
                        continue

                    try:
                        # 添加到session:
                        sessionMatch = db_session()
                        sessionMatch.add(new_match)
                        # 提交即保存到数据库:
                        sessionMatch.commit()

                        print('>>> 成功添加比赛！开始保存比赛详情...')

                        try:
                            conn.request('POST', reqMethodPlayGetplaydetail,
                                         AddcRand(reqPlayGetPlaydetailPayload + '&gameSeq=' + gameSeq+ '&gameSvrId=' + gameSvrId+ '&relaySvrId=' + relaySvrId+ '&roleId=' + roleId),
                                         headerdata)
                            playerListResponse = conn.getresponse()
                            playerListRes = playerListResponse.read()
                            playerListResData = json.loads(playerListRes.decode('utf-8'))

                            # print(playerListResData)

                            acntcampBlue = playerListResData['data']['acntcampBlue']
                            acntcampRed = playerListResData['data']['acntcampRed']
                            myPlayCamp = playerListResData['data']['myPlayCamp']
                            if myPlayCamp == 'red':
                                dataTOur = playerListResData['data']['dataRed']
                                dataThey = playerListResData['data']['dataBlue']
                                redSide = 1
                                blueSide = 2
                            else:
                                dataTOur = playerListResData['data']['dataBlue']
                                dataThey = playerListResData['data']['dataRed']
                                redSide = 2
                                blueSide = 1

                            # print('准备保存比赛详情...')
                            matchdDetail = MatchDetail()
                            matchdDetail.gameSeq=gameSeq
                            matchdDetail.gameSvrId=gameSvrId
                            matchdDetail.relaySvrId=relaySvrId
                            matchdDetail.killCntOur=dataTOur['killCnt']
                            matchdDetail.killCntThey=dataThey['killCnt']
                            matchdDetail.deadCntOur=dataTOur['deadCnt']
                            matchdDetail.deadCntThey=dataThey['deadCnt']
                            matchdDetail.assistCntOur=dataTOur['assistCnt']
                            matchdDetail.assistCntThey=dataThey['assistCnt']
                            matchdDetail.ldragonCntOur=dataTOur['ldragonCnt']
                            matchdDetail.ldragonCntThey=dataThey['ldragonCnt']
                            matchdDetail.bdragonCntOur=dataTOur['bdragonCnt']
                            matchdDetail.bdragonCntThey=dataThey['bdragonCnt']
                            matchdDetail.moneyOur=dataTOur['money']
                            matchdDetail.moneyThey=dataThey['money']
                            matchdDetail.multiCampRankOur=dataTOur['multiCampRank']
                            matchdDetail.multiCampRankThey=dataThey['multiCampRank']

                            try:
                                # 添加到session:
                                sessionMatchDetail = db_session()
                                sessionMatchDetail.add(matchdDetail)
                                # 提交即保存到数据库:
                                sessionMatchDetail.commit()
                                print('>>> 比赛详情matchdDetail保存完毕')
                            except Exception as e:
                                    print('  出现异常：%s' % repr(e))
                            finally:
                                sessionMatchDetail.close()

                            print('>>>> 准备保存参与比赛的玩家信息...')

                            if blueSide == 1:
                                for tmp_player in acntcampBlue:
                                    thisPlayer = AddPlayer(tmp_player)
                                    thisPlayer.gameSeq = gameSeq
                                    thisPlayer.gameSvrId = gameSvrId
                                    thisPlayer.relaySvrId = relaySvrId
                                    thisPlayer.teamSide = blueSide
                                    try:
                                        # 添加到session:
                                        sessionPlayer = db_session()
                                        sessionPlayer.add(thisPlayer)
                                        # 提交即保存到数据库:
                                        sessionPlayer.commit()
                                        print('>>>> 比赛成员详情蓝方['+thisPlayer.roleName+']保存完毕')
                                    except Exception as e:
                                        print('  出现异常：%s' % repr(e))
                                    finally:
                                        sessionPlayer.close()

                            else:
                                for tmp_player in acntcampRed:
                                    thisPlayer = AddPlayer(tmp_player)
                                    thisPlayer.gameSeq = gameSeq
                                    thisPlayer.gameSvrId = gameSvrId
                                    thisPlayer.relaySvrId = relaySvrId
                                    thisPlayer.teamSide = redSide
                                    try:
                                        # 添加到session:
                                        sessionPlayer = db_session()
                                        sessionPlayer.add(thisPlayer)
                                        # 提交即保存到数据库:
                                        sessionPlayer.commit()
                                        print('>>>> 比赛成员详情红方['+thisPlayer.roleName+']保存完毕')
                                    except Exception as e:
                                        print('  出现异常：%s' % repr(e))
                                    finally:
                                        sessionPlayer.close()

                        except Exception as e:
                            print('  出现异常：%s' % repr(e))
                        finally:
                            print('>>> 比赛详情保存完毕')

                    except Exception as e:
                        print('  出现异常：:%s' % repr(e))
                    finally:
                        print('>> 比赛保存完毕')
                        sessionMatch.close()

            except:
                print('出现异常：:\n%s' % traceback.format_exc())
                print('****** 获取比赛列表处理出错，该用户可能隐藏了战绩 ******')
            finally:
                print('************** 用户比赛记录处理完毕 **************')

    sessionDel = db_session()
    ten_mins_ago = current_time - datetime.timedelta(minutes=10)
    sessionDel.query(Members).filter(Members.updateDate < ten_mins_ago).delete()

except:
    print ('出现异常：:\n%s' % traceback.format_exc())
finally:
    print('处理完毕')
    sessionMember.close()
    sessionDel.close();

