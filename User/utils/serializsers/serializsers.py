from rest_framework import serializers
from User import models
from drf_dynamic_fields import DynamicFieldsMixin


class UserSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = "__all__"
class PlayUserNewSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    """
        新增(post) 删除(deletes) 玩家
    """
    success = serializers.SerializerMethodField()
    Proxy_UserName = serializers.SerializerMethodField()
    class Meta:
        model = models.PlayUser
        fields = ["success","Proxy_UserName","UserName","Proxy","SafeQuestion","SafeReply",]
        extra_kwargs = {'Proxy': {'write_only': True}}
    def get_success(self, obj):
        return True
    def get_Proxy_UserName(self,obj):
        return obj.Proxy.UserName

class PlayUserUpdataSerializer(PlayUserNewSerializer):
    """
        修改(put) 玩家
    """
    class Meta:
        model = models.PlayUser
        fields = ["Proxy_UserName","success","UserName","Assets","Wallet","Status","Proxy","ActualName","BankCardNum","DepositCount","DepositTotal","WithdrawalTotal","QQ","WeChat","Email","Phone",]
        extra_kwargs = {'Proxy': {'write_only': True}}

class PlayUserReadSerializer(PlayUserNewSerializer):
    """
        查(get) 玩家
    """
    class Meta:
        model = models.PlayUser
       # fields = ["success","Proxy_UserName","UserName","RegDate","Assets","Wallet","Status","QQ","WeChat","Email","Phone",]
        fields = "__all__"

class PlayUserDetailSerializer(PlayUserNewSerializer):
    """
        详查(get) 玩家
    """
    class Meta:
        model = models.PlayUser
        fields = "__all__"
        #fields = ["Proxy_UserName","success","ActualName","Proxy","RegDate","Wallet","Assets","DepositTotal","WithdrawalTotal","LastLoginDate","Status","UserName","Phone","Email","QQ","Gender","Birthday","WeChat","BankCardNum","LastLoginIpAddress","DepositCount","Language",]



class AgentNewSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    """
        新增(post) 删除(deletes) 玩家
    """
    success = serializers.SerializerMethodField()
    AgentId_UserName = serializers.SerializerMethodField()
    class Meta:
        model = models.Agent
        fields = "__all__"
        #fields = ["success","AgentId_UserName","UserName","AgentId","SafeQuestion","SafeReply",]
        extra_kwargs = {'AgentId': {'write_only': True}}
    def get_success(self, obj):
        return True
    def get_AgentId_UserName(self,obj):
        if obj.ProxyLevel == 0: # 总代理
            return "总代理"
        else:
            return obj.AgentId.UserName

class AgentUpdataSerializer(AgentNewSerializer):
    """
        改(put) 玩家
    """
    class Meta:
        model = models.Agent
        fields = ["success","ActualName","AgentId_UserName","UserName","AccountBalance","CommissionTotal","PromotionCode","RegDate","LastLoginIpAddress","Gender","Birthday","Email","QQ","WeChat","Email","Phone",]
        extra_kwargs = {'AgentId': {'write_only': True}}

class AgentReadSerializer(AgentNewSerializer):
    """
        查(get) 玩家
    """
    class Meta:
        model = models.Agent
        fields = "__all__"
        #fields = ["success","ActualName","AgentId_UserName","UserName","AccountBalance","CommissionTotal","RegDate",]

class AgentDetailSerializer(AgentNewSerializer):
    """
        祥查(get) 玩家
    """
    class Meta:
        model = models.Agent
        fields = "__all__"
       # fields = ["success","ActualName","AgentId_UserName","UserName","AccountBalance","CommissionTotal","PromotionCode","RegDate","LastLoginIpAddress","Gender","Birthday","Email","QQ","WeChat","Email","Phone",]











