from django.urls import path
from django.conf.urls import url

from . import views

app_name = "haq"

urlpatterns = [
    path('', views.AboutView, name="about"),
    path('about/', views.AboutView, name="about"),
    path('index/', views.IndexView, name="index"),  #this is reference
    path('books/', views.BookView, name="books"),
    path('searchRef/', views.SearchRefView, name="searchRef"),
    path('bookSearch/', views.BookSearchView, name="bookSearch"),
    path('bookAdd/', views.BookAddView, name="bookAdd"),
    path('bookSectOption/', views.BookSectOptionView, name="bookSectOption"),
    path('topicSearch/', views.TopicSearchView, name="topicSearch"),
    path('getTopic/', views.GetTopicView, name="getTopic"),
    url(r'^(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),
    path('personalitySearch/', views.PersonalitySearchView, name="personalitySearch"),
    path('logout', views.LogOutView, name="logout"),
    path('osample', views.OSampleView, name="osample"),
]

