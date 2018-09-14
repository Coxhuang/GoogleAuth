import django_filters
from User import models
from django.db.models import Q


class agentFilter(django_filters.rest_framework.FilterSet):
    # RegDate_gte = django_filters.DateFromToRangeFilter(field_name='user__LastLoginDate', lookup_expr='gte')
    username = django_filters.CharFilter(field_name="username")
    ActualName = django_filters.CharFilter(field_name='ActualName')
    class Meta:
        model = models.UserProfile
        fields = ["username","ActualName"]




class playerFilter(django_filters.rest_framework.FilterSet):
    usernames = django_filters.CharFilter(method='username_filter', label='usernames')
    RegDate_gte = django_filters.DateFromToRangeFilter(field_name='RegDate', lookup_expr='gte')
    BankCardNum = django_filters.CharFilter(field_name='BankCardNum')
    ActualName = django_filters.CharFilter(field_name='ActualName')
    class Meta:
        model = models.UserProfile
        fields = ["BankCardNum","ActualName","RegDate_gte"]
    def username_filter(self, queryset, name, value):
        q = Q()
        q.connector = 'OR'
        for foo in value.split(","):
            q.children.append(('username',foo))
        queryset = models.UserProfile.objects.filter(q)
        return queryset


