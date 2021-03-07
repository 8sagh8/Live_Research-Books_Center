
from django.contrib import admin
from django.urls import path, include
# this is to use URL i/o of PATH below
from django.conf.urls import url 

#from serverAPI import API & VIEWS
from serverAPI.api import *
from . import views

app_name = "serverAPI"

urlpatterns = []