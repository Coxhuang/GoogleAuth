from User import models
from apps.User.utils.groups import group
from apps.User.remoney import serializerRe
from django.shortcuts import get_object_or_404
from apps.User.utils.judges import judge
"""
初始化
"""


"""初始化用户"""
def initUser():
    obj = models.UserProfile.objects.create_user(id=1, username="admin_default", email="admin@admin.com", password="cox123456", Role="00001")
    group.addGroups(obj, "admin")

    obj = models.UserProfile.objects.create_user(id=2, username="server_default", email="server@server.com",password="cox123456", Role="00001")
    group.addGroups(obj, "server")

    obj = models.UserProfile.objects.create_user(id=3, username="topagent_default", email="topagent@topagent.com",password="cox123456", Role="10001")
    obj_top = models.Agent.objects.get_or_create(user=obj)
    if obj_top[1]:
        obj_top[0].CommissionProgram = get_object_or_404(models.ReMomeyGroup,groupName="ReMoneyScheme_default")
        obj_top[0].save()
    group.addGroups(obj, "topagent")

    obj = models.UserProfile.objects.create_user(id=4, username="agent_default", email="agent@agent.com", password="cox123456",Role="10002")
    obj_agent = models.Agent.objects.get_or_create(user=obj, Proxy=obj_top[0])
    if obj_agent[1]:
        obj_agent[0].CommissionProgram = get_object_or_404(models.ReMomeyGroup, groupName="ReMoneyScheme_default")
        obj_agent[0].save()
    group.addGroups(obj, "agent")

    obj = models.UserProfile.objects.create_user(id=5, username="player_default", email="player@player.com",password="cox123456", Role="20001")
    models.PlayUser.objects.get_or_create(user=obj, Proxy=obj_agent[0])
    group.addGroups(obj, "player")

    return None


"""初始化返佣方案"""
def initReMoneyScheme():
    """
        1.判断表中是否有 ReMoneyScheme_default 数据
        2.有: 不创建
        3.无: 创建默认返佣方案
    :return:
    """
    ReMomeyDict = [
        {
            "reName": "返佣1",
            "investHightLim": 1000,
            "comments": "haha54848",
            "availInvestCount": 2000,
            "investLowerLim": 5222,
            "reRatio": 12
        },
        {
            "reName": "返佣2",
            "investHightLim": 1000,
            "comments": "haha54848",
            "availInvestCount": 2000,
            "investLowerLim": 5222,
            "reRatio": 12
        },
        {
            "reName": "返佣3",
            "investHightLim": 1000,
            "comments": "haha54848",
            "availInvestCount": 2000,
            "investLowerLim": 5222,
            "reRatio": 12
        }
    ]
    obj_default = models.ReMomeyGroup.objects.get_or_create(groupName="ReMoneyScheme_default")
    if obj_default[1]: # 如果返佣表没有默认返佣方案
        for foo in ReMomeyDict:
            serializer = serializerRe.createReSchemeSerializer(data=foo)
            serializer.is_valid(raise_exception=True)
            models.ReMoney.objects.get_or_create(remomeygroup=obj_default[0], **foo)


def initSetRegister():
    """
    初始化注册填选项
    :return: None
    """
    dic = {
        "SetRegisterOptionData":
        {
            "email": 1,
            "QQ": 1,
            "mobile": 1,
            "WeChat": 1,
            "ActualName": 1,
            "SafeQuestion": 1,
            "SafeReply": 1,
            "Language": 1,
            "gender": 1,
            "birth": 1
        },
        "SetRegisterMustOptionData":
        {
            "email": 0,
            "QQ": 0,
            "mobile": 0,
            "WeChat": 0,
            "ActualName": 0,
            "SafeQuestion": 0,
            "SafeReply": 0,
            "Language": 0,
            "gender": 0,
            "birth": 0
        }
    }
    judge.createOrUpdateSetRegister("SetRegisterOptionData",dic["SetRegisterOptionData"])
    judge.createOrUpdateSetRegister("SetRegisterMustOptionData",dic["SetRegisterMustOptionData"])