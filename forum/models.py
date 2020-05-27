""" Models of the Post service """ 
from django.db import models
from general.abstract_models import TimeStampsMixin, SoftDeleteMixin
from authentication.models import UserInfo
# Create your models here.
class Topic(TimeStampsMixin, SoftDeleteMixin):
    """ Topic of the forum """
    name = models.CharField(
        'Name of the topic',
        max_length = 45,
    )

    description = models.CharField(
        'Description of the topic',
        max_length = 45,
    )

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)

class State(TimeStampsMixin, SoftDeleteMixin):
    """State of the state"""
    name = models.CharField(
        'Name of the state',
        max_length = 45,
    )

    description = models.CharField(
        'Description of the state',
        max_length = 45,
    )
    
    def __str__(self):
        return '{}: {}'.format(self.name, self.description)

class Replies(TimeStampsMixin, SoftDeleteMixin):
    """Replies of the post"""
    message = models.CharField(
        'Name of the state',
        max_length = 500,
    )
    stars = models.IntegerField()

    created_by = models.ForeignKey(
        UserInfo,
        on_delete=models.CASCADE,
    )

    parent_id = models.ForeignKey(
        'self',
        on_delete =  models.CASCADE,
    )

    #principal_post = models.ForeignKey(
     #   Post,
      #  on_delete =models.CASCADE,
    #)
