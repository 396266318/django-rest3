# coding=utf-8
# /usr/bin/env python
'''
Author hx
Email xin.hu@servingcloud.com

date: 2020/9/16 15:45
desc:
'''

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import APIInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email', 'groups', 'username', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class APIInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Mate:
        model = APIInfo
        fields = "__all__"


class APISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIInfo
        fields = "__all__"