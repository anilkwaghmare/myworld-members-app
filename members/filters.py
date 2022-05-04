import django_filters

from .models import *

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Members
        fields = '__all__'

        