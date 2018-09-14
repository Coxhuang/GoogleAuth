"""
判断函数
"""
import re
from django.http import Http404
from django.shortcuts import get_object_or_404
from User import models
from apps.User.utils.exceptions import exception

def isOnlyDigitAlp(username=None, password=None):
    if len(username) > 12 or len(username) < 6:
        raise exception.myException500("用户名长度仅支持6-12位")
    if len(password) > 12 or len(password) < 6:
        raise exception.myException500("密码长度仅支持6-12位")
    if re.sub('[a-zA-Z0-9]', "", str(username) + str(password)) :
        raise exception.myException500("账号密码只能由字母数字组成")
    else :
        pass

def isLoginUser(user,path):
    """
    通过url中的id判断id与被修改者是否是同一个人
    :param user: 当前登录的用户
    :param path: url路径
    :return: 1/0/e
    """
    try:
        url_id = int(path.split("/")[-2])  # url中id的列表
        return (True if user.id == url_id else False)
    except:
        raise exception.myException500("登录用户与被修改用户不是同一人")



def filterOwnRole(user,path):
    """
    过滤同角色的非登录者
    :user: 当前登录用户的obj
    :path: url路径
    :return: 1/0/e
    """
    url_id = path.split("/")[-2]
    url_obj = get_object_or_404(models.UserProfile,id=int(url_id))
    if (not isLoginUser(user,path)) and (url_obj.Role == user.Role):
        raise Http404
    return

def createOrUpdateSetRegister(RegisterName,data):
    """
    注册模块专用,判断在setRegister中是否存在RegisterName数据,存在就更新,不存在创建
    :param RegisterName: 字段名
    :param data: 更新的数据 Or 创建的数据
    :return: 更新/创建后的 obj
    """
    queryset = models.setRegister.objects.filter(RegisterName=RegisterName)
    if queryset.first() == None:
        models.setRegister.objects.create(RegisterName=RegisterName)
    obj = models.setRegister.objects.filter(RegisterName=RegisterName).update(**data)
    return obj

def isSubclass(dict_1,dict_2):
    """
        判断dict_1是否是dict_2的子集
    :param dict_1: 小
    :param dict_2: 大
    :return: True Or Flase
    """
    dic = {}
    for k,v in dict_1.items():
        if v:
            dic[k] = 1
    return set(dic.items()).issubset(dict_2.items())

