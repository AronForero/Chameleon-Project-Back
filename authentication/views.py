"""This file handles the logic that will be executed when the endpoint are called"""
import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Login, Role, UserStatus, UserInfo
from .serializers import LoginSerializer, RoleSerializer, UserStatusSerializer, UserInfoSerializer, CreateNewUserSerializer

# Create your views here.
class LoginViewSet(viewsets.ModelViewSet):
    """
    This class will handle all the logic for the login users
    """
    permission_classes = (AllowAny,)
    queryset = Login.objects.filter(trashed=False)
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateNewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        object_exist = UserInfo.objects.filter(email=serializer.validated_data.get('email'))
        if len(object_exist) != 0:
            return Response({'detail': 'The given email is already in use'}, status=status.HTTP_400_BAD_REQUEST)
        login_created = Login.objects.create(
            username=serializer.validated_data.get('username'),
            password=serializer.validated_data.get('password')
        )
        login_created.save()

        user_created = UserInfo.objects.create(
            name=serializer.validated_data.get('name', ''),
            last_name=serializer.validated_data.get('last_name', ''),
            email=serializer.validated_data.get('email'),
        )
        user_created.save()
        return Response(self.serializer_class(login_created).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        # search the current login object, corresponding to the given id
        current_login = get_object_or_404(Login, id=kwargs.get('id'), trashed=False)
        # set trashed to true to soft-delete the item
        current_login.trashed = True
        current_login.trashed_at = datetime.datetime.now()
        # save the changes
        current_login.save()

        # same process with the info
        current_user_info = get_object_or_404(UserInfo, login=current_login)
        current_user_info.trashed = True
        current_user_info.save()

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

class TopicViewSet(viewsets.ModelViewSet):
    """
    Handles the logic (CRUD) for the Post Topics
    """
    permission_classes = (IsAuthenticated,)
    queryset = Topic.objects.filter(trashed=False)
    serializer_class = TopicSerializer

class StateViewSet(viewsets.ModelViewSet):
    """
    Handles the logic (CRUD) for the Post States
    """
    permission_classes = (IsAuthenticated,)
    queryset = State.objects.filter(trashed=False)
    serializer_class = StateSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD for the Post
    """
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.filter(trashed=False)
    serializer_class = PostSerializer
