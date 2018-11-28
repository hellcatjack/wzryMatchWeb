# -*- coding:utf-8 -*-

# 王者荣耀助手用户token
reqToken = ""
reqGroupId = ""
reqServerId = ""

# 获取战队成员列表
reqBaseGameGroupmembersPayload = ""
reqGameGroupmembersPayload = reqBaseGameGroupmembersPayload + "&token=" + reqToken + "&groupId=" + reqGroupId + "&serverId=" + reqServerId
# 获取成员比赛场次信息
reqBasePlayGetmatchlistPayload = ""
reqPlayGetmatchlistPayload = reqBasePlayGetmatchlistPayload + "&token=" + reqToken
# 获取成员比赛详情信息
reqBasePlayGetPlaydetailPayload = ""
reqPlayGetPlaydetailPayload = reqBasePlayGetPlaydetailPayload + "&token=" + reqToken
# 获取成员卡片
reqBaseGetRoleCardPayload = ""
reqGetRoleCardPayload = reqBaseGetRoleCardPayload + "&token=" + reqToken
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