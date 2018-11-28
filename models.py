# -*- coding: utf-8 -*-

import datetime
from sqlalchemy import Column, String, Text, Integer,DateTime
from database import Base



# 定义User对象:
class Members(Base):
    # 表的名字:
    __tablename__ = 'members'

    # 表的结构:
    roleId = Column(String(100), primary_key=True)
    roleName = Column(String(100))
    roleDesc = Column(String(100))
    roleIcon = Column(String(255))
    nickname = Column(String(100))
    sex = Column(Integer)
    rank = Column(Integer)
    updateDate = Column(DateTime, default=datetime.datetime.now)

class Matchs(Base):
    # 表的名字:
    __tablename__ = 'matchs'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    roleId = Column(String(100))
    dteventtime = Column(Integer)
    gametype = Column(String(100))
    wincamp = Column(String(100))
    gametime = Column(String(100))
    killcnt = Column(String(100))
    deadcnt = Column(String(100))
    assistcnt = Column(String(100))
    gameresult = Column(String(100))
    mvpcnt = Column(String(100))
    losemvp = Column(String(100))
    heroId = Column(String(100))
    AcntCamp = Column(String(100))
    mapName = Column(String(100))
    # detailUrl = Column(String(255))
    rampage = Column(String(100))
    gameSvrId = Column(String(100))
    relaySvrId = Column(String(100))
    gameSeq = Column(String(100))
    pvpType = Column(Integer)
    multiCampRank = Column(String(100))
    battleType = Column(Integer)
    branchEvaluate = Column(Integer)
    oldMasterMatchScore = Column(String(100))
    newMasterMatchScore = Column(String(100))
    battleRoyaleEvaluate = Column(String(100))
    desc = Column(String(100))
    # heroIcon = Column(String(255))


class MatchDetail(Base):
    # 表的名字:
    __tablename__ = 'matchdetail'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    gameSeq = Column(String(100))
    gameSvrId = Column(String(100))
    relaySvrId = Column(String(100))
    killCntOur = Column(Integer)
    killCntThey = Column(Integer)
    deadCntOur = Column(Integer)
    deadCntThey = Column(Integer)
    assistCntOur = Column(Integer)
    assistCntThey = Column(Integer)
    ldragonCntOur = Column(Integer)
    ldragonCntThey = Column(Integer)
    bdragonCntOur = Column(Integer)
    bdragonCntThey = Column(Integer)
    moneyOur = Column(Integer)
    moneyThey = Column(Integer)
    multiCampRankOur = Column(Integer)
    multiCampRankThey = Column(Integer)



class Players(Base):
    # 表的名字:
    __tablename__ = 'players'

    # 表的结构:
    id = Column(Integer,primary_key=True)
    gameSeq = Column(String(100))
    gameSvrId = Column(String(100))
    relaySvrId = Column(String(100))
    teamSide = Column(Integer)
    roleId = Column(String(100))
    roleName = Column(String(100))
    heroName = Column(String(100))
    userId = Column(String(100))
    heroId = Column(String(100))
    killCnt = Column(String(100))
    deadCnt = Column(String(100))
    assistCnt = Column(String(100))
    totalOutputPerMin = Column(String(100))
    totalHurtHeroCntPerMin = Column(String(100))
    totalBeHurtedCntPerMin = Column(String(100))
    hero1TripleKillCnt = Column(String(100))
    godLikeCnt = Column(String(100))
    winMvp = Column(String(100))
    hero1UltraKillCnt = Column(String(100))
    hero1RampageCnt = Column(String(100))
    loseMvp = Column(String(100))
    hero1GhostLevel = Column(String(100))
    disGradeLevelId = Column(String(100))
    gradeLevelId = Column(String(100))
    gradeLevel = Column(String(100))
    finalEquipmentInfo = Column(Text)
    maxKill = Column(String(100))
    maxHurt = Column(String(100))
    maxAssist = Column(String(100))
    maxTower = Column(String(100))
    maxBeHurt = Column(String(100))
    heroSkillID = Column(String(100))
    heroSkillIcon = Column(String(255))
    heroIcon = Column(String(255))
    gradeGame = Column(String(100))
    totalHurtPercent = Column(String(100))
    totalHurtHeroCntPercent = Column(String(100))
    totalBeHurtedCntPercent = Column(String(100))
    acntcamp = Column(String(100))
    playerId = Column(String(100))
    gameScore = Column(String(100))
    branchEvaluate = Column(String(100))
    heroPosition = Column(String(100))
    usedtime = Column(String(100))
    newGrow = Column(String(100))
    newBattle = Column(String(100))
    newSurvive = Column(String(100))
    newHurtHero = Column(String(100))
    newKDA = Column(String(100))
    maxMvpScore = Column(String(100))
    totalWinNum = Column(String(100))
    totalLostNum = Column(String(100))
    avgMvpScore = Column(String(100))
    isMI = Column(String(100))
    oldMasterMatchScore = Column(String(100))
    newMasterMatchScore = Column(String(100))
    defeatAcntRatio = Column(String(100))
    joinGamePercent = Column(String(100))
    sabcgrow = Column(String(100))
    sabcbattle = Column(String(100))
    sabcsurvive = Column(String(100))
    sabchurtHero = Column(String(100))
    sabcKDA = Column(String(100))
    battleRoyaleEvaluate = Column(String(100))
    battleRoyaleTotalTeamNum = Column(String(100))
    battleRoyaleGrade = Column(String(100))
    battleRoyaleTimeToLive = Column(String(100))
    battleRoyaleGrowValue = Column(String(100))
    heroScoreGrade = Column(Text)
    hornorPercent = Column(String(100))
