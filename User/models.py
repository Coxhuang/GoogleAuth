from django.db import models
from django.contrib.auth.models import AbstractUser


class setRegister(models.Model):
    RegisterName = models.CharField(max_length=128, verbose_name="分类", unique=True)
    ActualName = models.BooleanField(verbose_name="真实姓名", default=False)
    mobile = models.BooleanField(verbose_name="手机号码", default=False)
    email = models.BooleanField(verbose_name="邮箱", default=False)
    QQ = models.BooleanField(verbose_name="QQ", default=False)
    SafeQuestion = models.BooleanField(verbose_name="安全问题", default=False)
    SafeReply = models.BooleanField(verbose_name="安全密码", default=False)
    Language = models.BooleanField(verbose_name="主语言", default=False)
    gender = models.BooleanField(verbose_name="性别", default=False)
    birth = models.BooleanField(verbose_name="生日", default=False)
    WeChat = models.BooleanField(verbose_name="微信", default=False)


class ReMomeyGroup(models.Model):
    "返佣方案"
    groupName = models.CharField(max_length=128, unique=True)
    RegDate = models.DateField(auto_now_add=True, verbose_name="创建时间")
    comments = models.CharField(max_length=128, verbose_name="备注", null=True, blank=True)

    def __str__(self):
        return self.groupName


class ReMoney(models.Model):
    "详细返佣"
    remomeygroup = models.ForeignKey(ReMomeyGroup, on_delete=models.CASCADE, related_name="remomeygroups")
    reName = models.CharField(max_length=64, verbose_name="方案名称")
    investHightLim = models.BigIntegerField(verbose_name="方案有效投注上限", default=999999999999)
    investLowerLim = models.BigIntegerField(verbose_name="方案有效投注下限", default=0)
    availInvestCount = models.IntegerField(verbose_name="有效投注人数")
    reRatio = models.FloatField(verbose_name="返佣比例")
    comments = models.CharField(max_length=128, verbose_name="备注", null=True, blank=True)
    RegDate = models.DateField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.reName

    class Meta:
        unique_together = ('reName', 'remomeygroup',)


SafeQuestion_Cho = (
    (0, u"这是一个test"),
    (1, u"这是一个test")
)


class UserProfile(AbstractUser):
    Role_Type = (('00001', u'工作人员'),
                 ('10001', u'总代理'),
                 ('10002', u'分代理'),
                 ('20001', u'普通用户'))
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    Language_Cho = (
        (0, u'简体中文'),
    )
    Role = models.CharField(max_length=16, default="00001")
    birth = models.DateField(verbose_name=u"生日", null=True, blank=True)
    ActualName = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'真实姓名')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="female", verbose_name=u"性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name=u"电话", help_text=u"电话号码")
    email = models.EmailField(max_length=100, blank=True, verbose_name=u"邮箱")
    QQ = models.CharField(max_length=20, null=True, verbose_name=u'qq号码')
    SafeQuestion = models.IntegerField(choices=SafeQuestion_Cho, default=0, verbose_name=u'安全问题')
    SafeReply = models.CharField(max_length=20, null=True, verbose_name=u'安全回答  ')
    WeChat = models.CharField(max_length=50, null=True, verbose_name=u'微信号码')
    BankCardNum = models.CharField(max_length=50, null=True, verbose_name=u'银行卡号')
    LastLoginIpAddress = models.GenericIPAddressField(default='0.0.0.0', verbose_name=u'最后登录ip')
    Language = models.IntegerField(choices=Language_Cho, default=0, verbose_name=u'语言')
    LastLoginDate = models.DateTimeField(auto_now_add=True, null=True, verbose_name=u'最后登录时间')
    RegDate = models.DateTimeField(auto_now_add=True, null=True, verbose_name=u'注册时间')

    def __str__(self):
        return self.username


class Agent(models.Model):
    Status_Cho = (
        (0, u'正常'),
        (1, u'待审核'),
        (2, u'审核失败'),
    )
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="agents")
    Proxy = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name=u'所属总代理', null=True, blank=True,
                              related_name="topagents")
    UserCount = models.IntegerField(default=0)
    CommissionTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    UserDeposit = models.IntegerField(default=0)
    MoneyDeposit = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Status = models.IntegerField(choices=Status_Cho, default=1)
    CommissionProgram = models.ForeignKey(ReMomeyGroup, on_delete=models.CASCADE, max_length=2, null=True,
                                          verbose_name="返佣方案", related_name="commissionprograms")
    AccountBalance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    PromotionCode = models.IntegerField(null=True)
    ProxyCount = models.IntegerField(default=0)
    PromotionURL = models.CharField(max_length=100, null=True)
    Funds = models.BigIntegerField(default=0)


class PlayUser(models.Model):
    Status_Cho = (
        (0, u'正常'),
        (1, u'冻结'),
        (2, u'账户异常')
    )
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name="playerusers", to_field='username')
    Proxy = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name=u'所属代理', null=True, blank=True,
                              related_name="proxyplayerusers")
    Wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Assets = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    DepositTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    WithdrawalTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Status = models.IntegerField(choices=Status_Cho, default=0)
    DepositCount = models.IntegerField(default=0)
    isBool = models.BooleanField(default=True, )

    def __str__(self):
        return self.user.username


class PlayerQuestions(models.Model):
    QuestionsType_Cho = (
        (0, u'提问'),
        (1, u'追问')
    )
    UserName = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='玩家账号', null=False,
                                 related_name="Playuser")
    QuestionsNumber = models.IntegerField(db_index=True)
    QuestionsTitle = models.CharField(max_length=256, blank=False)
    QuestionsText = models.TextField(blank=False)
    QuestionsTime = models.DateTimeField(auto_now_add=True)
    QuestionsType = models.IntegerField(default=0, choices=QuestionsType_Cho)
    IsReply = models.BooleanField(default=False)
    ReplyTime = models.DateTimeField(null=True)
    ReplyText = models.TextField(null=True)
    JobUser = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='工作人员', null=True,
                                related_name="Jobuser")

    def __str__(self):
        return self.QuestionsTitle

class Google2Auth(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    key = models.CharField(max_length=128,verbose_name="Google秘钥")