"""Endpoints of the users/authentication module"""
from django.urls import path
from .views import LoginViewSet

basic_ops_login = LoginViewSet.as_view({
    'post': 'create',
    'get': 'list',
})

modificate_login = LoginViewSet.as_view({
    'put': 'update',
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('user', basic_ops_login, name='create_list_users'),
    path('user/<int:id>', modificate_login, name='update_retrieve_delete'),
]