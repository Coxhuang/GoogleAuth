import django_filters
from User.models import PlayUser,Agent
from rest_framework import serializers

class PlayUserFilter(django_filters.rest_framework.FilterSet):
    """
        http://127.0.0.1:8000/Api/User/playuser_api_search/?RegDate_gte_after=2018-07-18&RegDate_gte_before=2018-07-20
    """
    RegDate_gte = django_filters.DateFromToRangeFilter(field_name='RegDate', lookup_expr='gte')
    class Meta:
        model = PlayUser
        #fields = ['UserName', 'Proxy__UserName','BankCardNum','ActualName','RegDate_gte',]
        fields = "__all__"


class AgentFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Agent
        fields = "__all__"
        #fields = ['UserName','ActualName',]