from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'findUser', views.find_user, name='findUser'),
    path(r'user/<int:user_id>', views.user_card, name='user')
]
