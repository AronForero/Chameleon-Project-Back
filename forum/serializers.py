from rest_framework import serializers
from forum.models import Topic, State

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        exclude = []

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        exclude = []
