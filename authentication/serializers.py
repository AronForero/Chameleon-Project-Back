from rest_framework import serializers
from authentication.models import Login, UserStatus, UserInfo, Role

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        exclude = ['password']

class UserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStatus
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    login = LoginSerializer()
    status = UserStatusSerializer()
    role = RoleSerializer()

    class Meta:
        model = UserInfo
        fields = '__all__'