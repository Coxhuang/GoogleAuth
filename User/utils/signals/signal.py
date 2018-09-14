from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db.backends.signals import connection_created
from django.db.models.signals import pre_migrate, post_migrate
from User import models
from apps.User.utils.inits import init

def addUserCount(obj):
    obj.ProxyCount += 1
    obj.save()
    return None


@receiver(post_save, sender=models.PlayUser)
def signalPlayerCreate(sender, *args,**kwargs):
    addUserCount(kwargs["instance"].Proxy)

@receiver(post_save, sender=models.Agent)
def signalAgentCreate(sender, *args,**kwargs):
    """
        创建分代理时,create agent进来一次
        保存分代理对应的总代理时,又save()一次,所以创建分代理时,出发两次信号量函数
    """
    if kwargs["instance"].user.Role == "10002": # 新增分代理
        addUserCount(kwargs["instance"].Proxy) # 总代理的下属分代理数目自增
    elif kwargs["instance"].user.Role == "10001": # 新增总代理
        pass
    else:
        pass


@receiver(post_migrate)
def callback2(sender, **kwargs):
    init.initReMoneyScheme() # 初始化默认返佣方案
    init.initSetRegister()  # 初始化注册设置
    init.initUser() # 初始化User


