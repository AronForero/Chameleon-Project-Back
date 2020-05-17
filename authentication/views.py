"""This file handles the logic that will be executed when the endpoint are called"""
import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Login, Role, UserStatus, UserInfo
from .serializers import LoginSerializer, RoleSerializer, UserStatusSerializer, UserInfoSerializer

# Create your views here.
class LoginViewSet(viewsets.ModelViewSet):
    """
    This class will handle all the logic for the login users
    """
    permission_classes = (AllowAny,)
    queryset = Login.objects.filter(trashed=False)
    serializer_class = LoginSerializer

    def destroy(self, request, *arg, **kwargs):
        current_login = get_object_or_404(Login, id=kwargs.get('id'))
        current_login.trashed = True
        current_login.trashed_at = datetime.datetime.now()
        current_login.save()
        return Response({'details': 'eliminacion exitosa'}, status=status.HTTP_200_OK)


class RoleViewSet(viewsets.ModelViewSet):
    """
    Handles the logic (CRUD) for the Roles
    """
    permission_classes = (IsAuthenticated,)
    queryset = Role.objects.filter(trashed=False)
    serializer_class = RoleSerializer


class UserStatusViewSet(viewsets.ModelViewSet):
    """
    CRUD for the user status
    """
    permission_classes = (IsAuthenticated,)
    queryset = UserStatus.objects.filter(trashed=False)
    serializer_class = UserStatusSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    """
    CRUD for the user Info
    """
    permission_classes = (IsAuthenticated,)
    queryset = UserInfo.objects.filter(trashed=False)
    serializer_class = UserInfoSerializer
