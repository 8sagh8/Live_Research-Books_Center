"""YaMehdiData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# this is to use URL i/o of PATH in 'urlpatterns = []'
from django.conf.urls import url 
#from serverAPI import views
from serverAPI.api import *

urlpatterns = [
    path('admin/', admin.site.urls),    #route to ADMIN Page only
    path('', include('mainpage.urls')), #route to Main Login Page only
    path('home/', include('haq.urls')), #route to Haq About Page only
    
    # path to serverAPI
    path('rest_api/authPerson_list/', AuthPersonList.as_view(), name='authPerson_list'),
    path('rest_api/topics_list/', TopicList.as_view(), name='topics_list'),
    path('rest_api/categories_list/', CategoryList.as_view(), name='topics_list'),
    path('rest_api/statuss_list/', StatusList.as_view(), name='topics_list'),
    path('rest_api/religions_list/', ReligionList.as_view(), name='topics_list'),
    path('rest_api/persons_list/', PersonList.as_view(), name='topics_list'),
    path('rest_api/needs_list/', NeedList.as_view(), name='topics_list'),
    path('rest_api/languages_list/', LanguageList.as_view(), name='topics_list'),
    path('rest_api/books_list/', BookList.as_view(), name='topics_list'),
    path('rest_api/references_list/', ReferenceList.as_view(), name='topics_list'),

]
