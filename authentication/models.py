""" Models of the Users/Authentication service """ 
from django.db import models
from general.abstract_models import TimeStampsMixin, SoftDeleteMixin

# Create your models here.

class Login(TimeStampsMixin, SoftDeleteMixin):
    """ Table Login, will handle the login info, to sing into the forum """
    username = models.CharField(
        'nombre del usuario',
        max_length=50,
    )

    password = models.CharField(
        'Password',
        max_length=20,
    )

    def __str__(self):
        return '{}'.format(self.username)


class UserStatus(TimeStampsMixin, SoftDeleteMixin):
    """ State of the User... Can be replaced by a new CharField with choices in user info """
    status = models.CharField(
        'State of the User',
        max_length = 20,
    )
    description = models.CharField(
        'Description of the User status',
        max_length=200,
    )

    def __str__(self):
        return '{}: {}'.format(self.status, self.description)
    


class Role(TimeStampsMixin, SoftDeleteMixin):
    """ Roles that can have the users """
    nombre = models.CharField(
        'Role of the User',
        max_length = 20,
    )

    description = models.CharField(
        'Description of the User role',
        max_length=200,
    )

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)


class UserInfo(TimeStampsMixin, SoftDeleteMixin):
    """ User personal information """
    name = models.CharField(
        'Name of the person',
        max_length=50,
    )

    last_name = models.CharField(
        'Lastname of the person',
        max_length=50,
    )

    age = models.IntegerField()

    email = models.EmailField(
        max_length=200,
    )

    signature = models.TextField()

    login = models.ForeignKey(
        Login,
        on_delete=models.CASCADE
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )

    status = models.ForeignKey(
        UserStatus,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '{} {}, Email: {}, Edad: {}, Rol: {}, Estado: {}'.format(self.name, self.last_name, self.email, self.age, self.role, self.status)
    
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





