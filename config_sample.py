# -*- coding:utf-8 -*-

# 王者荣耀助手用户token
reqGroupId = ""
reqServerId = ""

reqToken = ""
reqUserId= ""
reqMyRoleId = ""

# 获取战队成员列表
reqBaseGameGroupmembersPayload = "gameId=20001&groupType=1&areaId=3&apiVersion=2&cChannelId=3&cClientVersionCode=2018092902&cClientVersionName=2.36.105&cCurrentGameId=20001&cDeviceCPU=armeabi-v7a%24armeabi&cDeviceId=9ca2c8f3ca17a3494145b6726e1fa4a2da1e029c&cDeviceImei=868663032496636&cDeviceMac=02%3A00%3A00%3A00%3A00%3A00&cDeviceMem=113853&cDeviceModel=MIX%202S&cDeviceNet=WIFI&cDevicePPI=440&cDeviceSP=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&cDeviceScreenHeight=2030&cDeviceScreenWidth=1080&cGameId=20001&cGzip=1&cRand=1542071519010&cSystem=android&cSystemVersionCode=26&cSystemVersionName=8.0.0&gameId=20001"
reqGameGroupmembersPayload = reqBaseGameGroupmembersPayload + "&token=" + reqToken + "&groupId=" + reqGroupId + "&serverId=" + reqServerId + "&userId=" + reqUserId
# 获取成员比赛场次信息
reqBasePlayGetmatchlistPayload = "gameId=20001&lastTime=0&apiVersion=4&isMI=0&cChannelId=3&cClientVersionCode=2018092902&cClientVersionName=2.36.105&cCurrentGameId=20001&cDeviceCPU=armeabi-v7a%24armeabi&cDeviceId=9ca2c8f3ca17a3494145b6726e1fa4a2da1e029c&cDeviceImei=868663032496636&cDeviceMac=02%3A00%3A00%3A00%3A00%3A00&cDeviceMem=113853&cDeviceModel=MIX%202S&cDeviceNet=WIFI&cDevicePPI=440&cDeviceSP=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&cDeviceScreenHeight=2030&cDeviceScreenWidth=1080&cGameId=20001&cGzip=1&cSystem=android&cSystemVersionCode=26&cSystemVersionName=8.0.0&gameId=20001"
reqPlayGetmatchlistPayload = reqBasePlayGetmatchlistPayload + "&token=" + reqToken + "&userId=" + reqUserId
# 获取成员比赛详情信息
reqBasePlayGetPlaydetailPayload = "gameId=20001&AcntCamp=1&battleType=25&pvpType=5&cChannelId=3&cClientVersionCode=2018092902&cClientVersionName=2.36.105&cCurrentGameId=20001&cDeviceCPU=armeabi-v7a%24armeabi&cDeviceId=9ca2c8f3ca17a3494145b6726e1fa4a2da1e029c&cDeviceImei=868663032496636&cDeviceMac=02%3A00%3A00%3A00%3A00%3A00&cDeviceMem=113853&cDeviceModel=MIX%202S&cDeviceNet=WIFI&cDevicePPI=440&cDeviceSP=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&cDeviceScreenHeight=2030&cDeviceScreenWidth=1080&cGameId=20001&cGzip=1&cRand=1542072120866&cSystem=android&cSystemVersionCode=26&cSystemVersionName=8.0.0&gameId=20001"
reqPlayGetPlaydetailPayload = reqBasePlayGetPlaydetailPayload + "&token=" + reqToken + "&userId=" + reqUserId
# 获取成员卡片
reqBaseGetRoleCardPayload = "gameId=20001&apiVersion=4&versioncode=2018092902&platType=android&cChannelId=3&cClientVersionCode=2018092902&cClientVersionName=2.36.105&cCurrentGameId=20001&cDeviceCPU=armeabi-v7a%24armeabi&cDeviceId=9ca2c8f3ca17a3494145b6726e1fa4a2da1e029c&cDeviceImei=868663032496636&cDeviceMac=02%3A00%3A00%3A00%3A00%3A00&cDeviceMem=113853&cDeviceModel=MIX%202S&cDeviceNet=WIFI&cDevicePPI=440&cDeviceSP=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A&cDeviceScreenHeight=2030&cDeviceScreenWidth=1080&cGameId=20001&cGzip=1&cSystem=android&cSystemVersionCode=28&cSystemVersionName=9&gameId=20001"
reqGetRoleCardPayload = reqBaseGetRoleCardPayload + "&token=" + reqToken + "&myRoleId=" + reqMyRoleId + "&userId=" + reqUserId

# 接口地址
requrl = "ssl.kohsocialapp.qq.com:10001"
# 接口方法
reqMethodGameGroupmembers = "/game/groupmembers"
reqMethodPlayGetmatchlist = "/play/getmatchlist"
reqMethodPlayGetplaydetail = "/play/getplaydetail"
reqMethodGetRoleCard = "/game/rolecard"
# httpHeader
headerdata = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8", "noencrypt": "1"}

# 服务器IP以及端口
serverIp = '0.0.0.0'
serverPort = '8888'

# 是否执行比赛导入
isImport = True

# 更改token本地command地址
changeTokenPath = 'd:\\1.bat'