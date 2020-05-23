""" Models of the Post service """ 
from django.db import models
from general.abstract_models import TimeStampsMixin, SoftDeleteMixin

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