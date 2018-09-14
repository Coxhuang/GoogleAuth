from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import  mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from User import models
from django.contrib.auth import authenticate,login
import pyotp
from django.shortcuts import get_object_or_404
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from User.utils.exceptions import exception
import base64
import codecs
import random
import re
from User.utils.googleauths import totp
from django.shortcuts import render


"""
绑定Google客户端
"""




class googleBindAPI(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self,request):
        # value = request.data
        # try:username = value["username"]
        # except:username = None
        # try:email = value["email"]
        # except:email = None
        # password = value["password"]
        # user = authenticate(username=username, email=email, password=password)  # username 和 email 都可以登录
        # if user:
            # login(request, user)
            # base_32_secret = base64.b32encode(
            #     codecs.decode(codecs.encode(
            #         '{0:020x}'.format(random.getrandbits(80))
            #     ), 'hex_codec')
            # )
            # totp_obj = totp.TOTP(base_32_secret.decode("utf-8"))
            # qr_code = re.sub(r'=+$', '', totp_obj.provisioning_uri(request.user.email))
            #
            # obj_user = get_object_or_404(models.UserProfile, username=value["username"])
            # queryset = models.Google2Auth.objects.filter(user__username=value["username"])
            # if queryset.first() == None:
            #     models.Google2Auth.objects.create(user=obj_user)
            # key = str(base_32_secret,encoding="utf-8")
            # models.Google2Auth.objects.filter(user__username=value["username"]).update(key=key)
            qr_code = request.data["qr_code"]
            return render(request, 'configure1.html', {"qr_code": qr_code})
            # return Response({"code": status.HTTP_201_CREATED, "success": True, "msg": "绑定成功","results": {"qr_code": qr_code}}, status=status.HTTP_201_CREATED)
        # else:
        #     raise exception.myException500("账号密码不匹配")


def Google_Verify_Result(secret_key,verifycode):
    t = pyotp.TOTP(secret_key)
    result = t.verify(verifycode) #对输入验证码进行校验，正确返回True
    msg = result if result is True else False
    return msg


def add(request):

    models.UserProfile.objects.create_user(username="cox",email="cox@cox.com",password="cox123456")
    return HttpResponse("ooo")



"""
{
"username":"cox",
"password":"cox123456"
}
"""

