
from django.contrib import admin
from django.urls import path, include
# this is to use URL i/o of PATH below
from django.conf.urls import url 

#from serverAPI import API & VIEWS
from serverAPI.api import *
from . import views

app_name = "serverAPI"

urlpatterns = [
    path('intoJSON/', views.IntoJSONView, name='intoJSON'),

    # Because i have created URL for API in 'YaMehdiData' app's urls
    url(r'^api/topics_list/$', TopicsList.as_view(), name='topics_list'),

    # path('api/topics_list/$', include('serverAPI.urls')) #route to Main Login Page only
    
    # call data by user_id in database
    # url(r'^api/users_list/(?P<employee_id>\d+)$', UserDetail.as_view(), name='user_list'),

]