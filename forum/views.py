"""This file handles the logic that will be executed when the endpoint are called"""
from django.shortcuts import render
import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Topic,State
from .serializers import TopicSerializer, StateSerializer

# Create your views here.

class TopicViewSet(viewsets.ModelViewSet):
    """
    This class will handle all the logic for the Topics
    """

    permission_classes = (IsAuthenticated,)
    queryset = Topic.objects.filter(trashed=False)
    serializer_class = TopicSerializer

class StateViewSet(viewsets.ModelViewSet):
    """
    This class will handle all the logic for the State
    """

    permission_classes = (IsAuthenticated,)
    queryset = State.objects.filter(trashed=False)
    serializer_class = StateSerializer