from django.contrib.auth.models import Group
from django.http import Http404
from apps.User.utils.exceptions import exception
"""
批量添加用户组
"""

def addGroups(obj,role):
    group,created = Group.objects.get_or_create(name=role)
    group.user_set.add(obj)
    return None



def addJobGroups(obj,role):
    if role == "00001a": # admin
        addGroups(obj,"admin")
    elif role == "00001b": # server
        addGroups(obj,"server")
    else:raise exception.myException401("新建工作人员时,输入角色不正确")
