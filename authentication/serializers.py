from rest_framework import serializers
from authentication.models import Login, UserStatus, UserInfo, Role


class CreateNewUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=False)


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        exclude = ['password', 'created_at', 'updated_at', 'trashed', 'trashed_at']

class UserStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStatus
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']


class UserInfoSerializer(serializers.ModelSerializer):
    login = LoginSerializer()
    status = UserStatusSerializer()
    role = RoleSerializer()

    class Meta:
        model = UserInfo
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']

class PostSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    stars = serializers.IntegerField(required=False, allow_blank=False, allow_null=False)
    duplicated = serializers.BinaryField(required=True)
    created_by = serializers.UserInfoSerializer(required=True)
    topic = serializers.TopicSerializer(required=True, allow_blank=False, allow_null=False)
    state = serializers.StateSerializer(required=True, allow_blank=False, allow_null=False)
    duplicated_id = serializers.PrimaryKeyRelatedField(allow_null=True)

    class Meta:
        model = Post
        exclude = ['created_at', 'updated_at', 'trashed', 'trashed_at']
