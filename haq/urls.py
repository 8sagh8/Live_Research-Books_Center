from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = "haq"

urlpatterns = [
    path('books/', views.BookView, name="books"),
path('status/', views.StatusView, name="status"),
    path('getStatusBooks/', views.GetStatusBooksView, name="getStatusBooks"),

    path('', views.AboutView, name="about"),
    path('about/', views.AboutView, name="about"),
    path('index/', views.IndexView, name="index"),  #this is reference
    path('searchRef/', views.SearchRefView, name="searchRef"),
    path('categories/', views.CategoryView, name="categories"),
    path('languages/', views.LanguageView, name="languages"),
    path('needs/', views.NeedView, name="needs"),
    path('personalities/', views.PersonalityView, name="personalities"),
    path('religions/', views.ReligionView, name="religions"),
    url(r'status/(?P<status_id>[0-9]+)/$', views.GetStatusBooksView, name="getStatusBooks"),
    path('logout', views.LogOutView, name="logout"),

    # API routes
    path('intoJSON/', views.IntoJsonView, name="intoJSON"),

    # JSON Files routes
    path('createJSON', views.CreateJSONView, name="createJSON"),

    #  to work on below
    path('topicJSON/', views.TopicJSONView, name="topicJSON"),
    path('bookAdd/', views.BookAddView, name="bookAdd"),
    path('bookSectOption/', views.BookSectOptionView, name="bookSectOption"),
    path('topicSearch/', views.TopicSearchView, name="topicSearch"),
    # path('getTopic/', views.GetTopicView, name="getTopic"),
    url(r'topic/(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),
    path('personalitySearch/', views.PersonalitySearchView, name="personalitySearch"),
    path('osample', views.OSampleView, name="osample"),
]

