from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from api.serializers import UserSerializer, GroupSerializer
from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
            Return a user instance.

        list:
            Return all users, ordered by most recently joined.

        create:
            Create a new user.

        delete:
            Remove an existing user.

        partial_update:
            Update one or more fields on an existing user.

        update:
            Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
            Return a group instance.

        list:
            Return all groups, ordered by most recently joined.

        create:
            Create a new group.

        delete:
            Remove an existing group.

        partial_update:
            Update one or more fields on an existing group.

        update:
            Update a group.
        """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class APIList(generics.ListAPIView):
    """查看接口列表"""
    queryset = models.APIInfo.objects.all()
    serializers_class = serializers.APISerializer


class APIDetail(generics.RetrieveAPIView):
    """查看接口明细"""
    queryset = models.APIInfo.objects.all()
    serializers_class = serializers.APISerializer


class APIDetail(generics.RetrieveUpdateDestroyAPIView):
    """更新接口内容"""
    queryset = models.APIInfo.objects.all()
    serializers_class = serializers.APISerializer


class APIInfoViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            返回一组 (查)
        list:
            返回所有组
        create:
            创建新组
        delete:
            删除现有的一组
        partial_update:
            更新现有组中的一个或多个字段 && 更新部分内容
        update:
            更新一组，更新全部数据
    """
    queryset = models.APIInfo.objects.all()
    serializer_class = serializers.APISerializer