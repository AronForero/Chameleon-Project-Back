from rest_framework import serializers
from forum.models import Topic, State
from authentication.serializers import UserInfoSerializer

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        exclude = []

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = []



class RepliesSerializer(serializers.ModelSerializer):

    created_by =  UserInfoSerializer()  
    parent_id = UserInfoSerializer()
    
    class Meta:
        model= Replies
        exclude = []