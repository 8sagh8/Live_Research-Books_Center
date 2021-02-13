from django.urls import path
from django.conf.urls import url

from . import views

app_name = "haq"

urlpatterns = [
    path('', views.AboutView, name="about"),
    path('about/', views.AboutView, name="about"),
    path('index/', views.IndexView, name="index"),  #this is reference
    path('searchRef/', views.SearchRefView, name="searchRef"),
    path('books/', views.BookView, name="books"),
    path('bookSearch/', views.BookSearchView, name="bookSearch"),
    path('categories/', views.CategoryView, name="categories"),
    path('languages/', views.LanguageView, name="languages"),
    path('needs/', views.NeedView, name="needs"),
    path('personalities/', views.PersonalityView, name="personalities"),
    path('religions/', views.ReligionView, name="religions"),
    path('status/', views.StatusView, name="status"),


    path('bookAdd/', views.BookAddView, name="bookAdd"),
    path('bookSectOption/', views.BookSectOptionView, name="bookSectOption"),
    path('topicSearch/', views.TopicSearchView, name="topicSearch"),
    path('getTopic/', views.GetTopicView, name="getTopic"),
    url(r'^(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),
    path('personalitySearch/', views.PersonalitySearchView, name="personalitySearch"),
    path('logout', views.LogOutView, name="logout"),
    path('osample', views.OSampleView, name="osample"),
]

