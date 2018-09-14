"""
批量删除
    只有管理员具有删除权限
"""
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from User import models
from django.db.models import Q
from apps.User.utils.exceptions import exception




def delJobUser(request,role):
    url = request.path.split("/")[-2].split(",")  # url中id的列表
    for foo in url:
        obj_user = get_object_or_404(models.UserProfile, id=int(foo))
        try:
            obj_user.groups.get(name=role) # 要删除id对应的obj,是否属于group组
            obj_user.delete()
        except:pass





def delUser(request,model,role,top=None):
    url = request.path.split("/")[-2].split(",")  # url中id的列表
    for foo in url:
        obj_user = get_object_or_404(models.UserProfile,id=int(foo))
        if not obj_user.groups.filter(Q(name=role)|Q(name=top)): # 要删除id对应的obj,是否属于group组
            pass
        else:
            try:
                obj = get_object_or_404(model,user_id=obj_user.id) # 获取关联的用户表
            except:
                obj = get_object_or_404(model,user_id=obj_user.username) # 获取关联的用户表
            obj_user.delete()
            obj.delete()
