/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.7.24-0ubuntu0.18.04.1 : Database - teammatch
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`teammatch` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `teammatch`;

/*Table structure for table `heroimage` */

DROP TABLE IF EXISTS `heroimage`;

CREATE TABLE `heroimage` (
  `roleId` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `heroImg` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `useCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroGrade` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`roleId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*Table structure for table `matchdetail` */

DROP TABLE IF EXISTS `matchdetail`;

CREATE TABLE `matchdetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gameSeq` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gameSvrId` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `relaySvrId` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `killCntOur` int(11) DEFAULT NULL,
  `killCntThey` int(11) DEFAULT NULL,
  `deadCntOur` int(11) DEFAULT NULL,
  `deadCntThey` int(11) DEFAULT NULL,
  `assistCntOur` int(11) DEFAULT NULL,
  `assistCntThey` int(11) DEFAULT NULL,
  `ldragonCntOur` int(11) DEFAULT NULL,
  `ldragonCntThey` int(11) DEFAULT NULL,
  `bdragonCntOur` int(11) DEFAULT NULL,
  `bdragonCntThey` int(11) DEFAULT NULL,
  `moneyOur` int(11) DEFAULT NULL,
  `moneyThey` int(11) DEFAULT NULL,
  `multiCampRankOur` int(11) DEFAULT NULL,
  `multiCampRankThey` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_game` (`gameSeq`,`gameSvrId`,`relaySvrId`)
) ENGINE=MyISAM AUTO_INCREMENT=1887 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/*Table structure for table `matchs` */

DROP TABLE IF EXISTS `matchs`;

CREATE TABLE `matchs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roleId` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dteventtime` bigint(20) DEFAULT NULL,
  `gametype` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `wincamp` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gametime` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `killcnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `deadcnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `assistcnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gameresult` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mvpcnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `losemvp` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroId` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `AcntCamp` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mapName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rampage` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gameSvrId` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `relaySvrId` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gameSeq` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pvpType` int(11) DEFAULT NULL,
  `multiCampRank` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleType` int(11) DEFAULT NULL,
  `branchEvaluate` int(11) DEFAULT NULL,
  `oldMasterMatchScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newMasterMatchScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleRoyaleEvaluate` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `desc` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_match` (`gameSeq`,`gameSvrId`,`relaySvrId`),
  KEY `idx_time` (`dteventtime`)
) ENGINE=MyISAM AUTO_INCREMENT=1898 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/*Table structure for table `members` */

DROP TABLE IF EXISTS `members`;

CREATE TABLE `members` (
  `roleId` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `roleName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `roleDesc` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `roleIcon` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nickname` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`roleId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/*Table structure for table `players` */

DROP TABLE IF EXISTS `players`;

CREATE TABLE `players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gameSeq` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gameSvrId` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `relaySvrId` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `teamSide` int(11) DEFAULT NULL,
  `roleId` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `roleName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroName` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `userId` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroId` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `killCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `deadCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `assistCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalOutputPerMin` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalHurtHeroCntPerMin` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalBeHurtedCntPerMin` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hero1TripleKillCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `godLikeCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `winMvp` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hero1UltraKillCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hero1RampageCnt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `loseMvp` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hero1GhostLevel` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `disGradeLevelId` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gradeLevelId` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gradeLevel` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `finalEquipmentInfo` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxKill` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxHurt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxAssist` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxTower` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxBeHurt` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroSkillID` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroSkillIcon` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroIcon` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gradeGame` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalHurtPercent` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalHurtHeroCntPercent` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalBeHurtedCntPercent` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `acntcamp` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `playerId` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gameScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `branchEvaluate` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroPosition` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `usedtime` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newGrow` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newBattle` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newSurvive` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newHurtHero` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newKDA` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `maxMvpScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalWinNum` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `totalLostNum` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `avgMvpScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `isMI` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `oldMasterMatchScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `newMasterMatchScore` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `defeatAcntRatio` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `joinGamePercent` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sabcgrow` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sabcbattle` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sabcsurvive` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sabchurtHero` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `sabcKDA` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleRoyaleEvaluate` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleRoyaleTotalTeamNum` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleRoyaleGrade` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleRoyaleTimeToLive` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `battleRoyaleGrowValue` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heroScoreGrade` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `hornorPercent` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_player` (`gameSeq`,`gameSvrId`,`relaySvrId`,`roleId`)
) ENGINE=MyISAM AUTO_INCREMENT=12453 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci CHECKSUM=1 DELAY_KEY_WRITE=1 ROW_FORMAT=DYNAMIC;

/* Trigger structure for table `members` */

DELIMITER $$

/*!50003 DROP TRIGGER*//*!50032 IF EXISTS */ /*!50003 `trig_members_rank` */$$

/*!50003 CREATE */ /*!50017 DEFINER = 'hellcat'@'%' */ /*!50003 TRIGGER `trig_members_rank` BEFORE INSERT ON `members` FOR EACH ROW BEGIN
    
    DECLARE myRank INT;
	SET new.roleDesc = SUBSTRING_INDEX(NEW.roleDesc, ' ', -1);
	
	CASE new.roleDesc
	WHEN '青铜III' THEN 
	SET @myRank=1;
	WHEN '青铜II' THEN 
	SET @myRank=2;
	WHEN '青铜I' THEN 
	SET @myRank=3;
	WHEN '白银IV' THEN 
	SET @myRank=4;
	WHEN '白银III' THEN 
	SET @myRank=5;
	WHEN '白银II' THEN 
	SET @myRank=6;
	WHEN '白银I' THEN 
	SET @myRank=7;
	WHEN '黄金IV' THEN 
	SET @myRank=8;
	WHEN '黄金III' THEN 
	SET @myRank=9;
	WHEN '黄金II' THEN 
	SET @myRank=10;
	WHEN '黄金I' THEN 
	SET @myRank=11;
	WHEN '铂金IV' THEN 
	SET @myRank=12;
	WHEN '铂金III' THEN 
	SET @myRank=13;
	WHEN '铂金II' THEN 
	SET @myRank=14;
	WHEN '铂金I' THEN 
	SET @myRank=15;
	WHEN '钻石V' THEN 
	SET @myRank=16;
	WHEN '钻石IV' THEN 
	SET @myRank=17;
	WHEN '钻石III' THEN 
	SET @myRank=18;
	WHEN '钻石II' THEN 
	SET @myRank=19;
	WHEN '钻石I' THEN 
	SET @myRank=20;
	WHEN '星耀V' THEN 
	SET @myRank=21;
	WHEN '星耀IV' THEN 
	SET @myRank=22;
	WHEN '星耀III' THEN 
	SET @myRank=23;
	WHEN '星耀II' THEN 
	SET @myRank=24;
	WHEN '星耀I' THEN 
	SET @myRank=25;
	WHEN '最强王者' THEN 
	SET @myRank=26;
	WHEN '荣耀王者' THEN 
	SET @myRank=27;
	ELSE 
	SET @myRank=0;
	END CASE; 
	SET NEW.rank=@myRank;
END */$$


DELIMITER ;

/*!50106 set global event_scheduler = 1*/;

/* Event structure for event `importHeroImage` */

/*!50106 DROP EVENT IF EXISTS `importHeroImage`*/;

DELIMITER $$

/*!50106 CREATE DEFINER=`hellcat`@`%` EVENT `importHeroImage` ON SCHEDULE EVERY 1 DAY STARTS '2018-11-17 03:00:00' ON COMPLETION PRESERVE ENABLE DO begin
call createHeroInform;
end */$$
DELIMITER ;

/* Procedure structure for procedure `createHeroInform` */

/*!50003 DROP PROCEDURE IF EXISTS  `createHeroInform` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`hellcat`@`%` PROCEDURE `createHeroInform`()
BEGIN
DELETE FROM players WHERE roleId NOT IN (SELECT roleId FROM members);   
DELETE FROM heroimage;
INSERT INTO heroimage 
SELECT roleId,GROUP_CONCAT(heroIcon ORDER BY usecnt DESC) heroImg,GROUP_CONCAT(usecnt ORDER BY usecnt DESC),GROUP_CONCAT(avgGrade ORDER BY usecnt DESC),GROUP_CONCAT(heroName ORDER BY usecnt DESC) FROM (
SELECT 
  a.* 
FROM
  (SELECT aaa.*,@i:=@i+1 tmpcnt FROM (
SELECT 
    i.roleId,
    i.heroId,
    i.heroName,
    i.heroIcon,
    AVG(i.gradeGame) avgGrade,
    COUNT(1) usecnt 
  FROM
    players AS i
    LEFT JOIN members ii
    ON i.`roleId`=ii.`roleId`
    WHERE ii.`roleId` IS NOT NULL
  GROUP BY i.roleId,
    i.heroId 
ORDER BY roleId,usecnt) aaa,(SELECT @i:=0) bbb
) a LEFT JOIN (SELECT aaa.*,@iii:=@iii+1 tmpcnt FROM (
SELECT 
    i.roleId,
    i.heroId,
    i.heroName,
    i.heroIcon,
    AVG(i.gradeGame) avgGrade,
    COUNT(1) usecnt 
  FROM
    players AS i
    LEFT JOIN members ii
    ON i.`roleId`=ii.`roleId`
    WHERE ii.`roleId` IS NOT NULL
  GROUP BY i.roleId,
    i.heroId 
ORDER BY roleId,usecnt) aaa,(SELECT @iii:=0) bbb
) b
ON a.roleId=b.roleId AND a.tmpcnt < b.tmpcnt
GROUP BY a.roleId,a.heroId,a.usecnt 
HAVING COUNT(b.tmpcnt) < 3
ORDER BY a.roleId,a.usecnt DESC
) haha GROUP BY roleId;
    END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
