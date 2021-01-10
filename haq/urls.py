from django.urls import path
from django.conf.urls import url

from . import views

app_name = "haq"

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('about/', views.AboutView, name="about"),
    path('books/', views.BookView, name="books"),
    path('searchRef/', views.SearchRefView, name="searchRef"),
    path('bookSearch/', views.BookSearchView, name="bookSearch"),
    path('bookAdd/', views.BookAddView, name="bookAdd"),
    path('bookSectOption/', views.BookSectOptionView, name="bookSectOption"),
    path('topicSearch/', views.TopicSearchView, name="topicSearch"),
    path('personalitySearch/', views.PersonalitySearchView, name="personalitySearch"),
    path('logout', views.LogOutView, name="logout"),
]