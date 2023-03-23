from django.urls import re_path
from MTPapp import views

urlpatterns=[
    re_path(r'^$',views.users,name='users'),
]
