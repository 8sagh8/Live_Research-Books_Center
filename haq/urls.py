from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = "haq"

urlpatterns = [
    path('books/', views.BookView, name="books"),
    path('status/', views.StatusView, name="status"),
    url(r'getStatusBooks/(?P<status_id>[0-9]+)/$', views.GetStatusBooksView, name="getStatusBooks"),
    path('religions/', views.ReligionView, name="religions"),
    url(r'getReligiousBooks/(?P<sect_id>[0-9]+)/$', views.GetReligiousBooksView, name="getReligiousBooks"),
    path('need/', views.NeedView, name="need"),
    url(r'getNeedBooks/(?P<need_id>[0-9]+)/$', views.GetNeedBooksView, name="getNeedBooks"),
    path('languages/', views.LanguagesView, name="languages"),
    url(r'getLanguagesBooks/(?P<language_id>[0-9]+)/$', views.GetLanguagesBooksView, name="getLanguagesBooks"),
    path('categories/', views.CategoriesView, name="categories"),
    url(r'getCategoriesBooks/(?P<category_id>[0-9]+)/$', views.GetCategoriesBooksView, name="getCategoriesBooks"),
    path('topicSearch/', views.TopicSearchView, name="topicSearch"),
    url(r'getTopic/(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),

    path('', views.IndexView, name="index"),
    path('index/', views.IndexView, name="index"),
    path('about/', views.AboutView, name="about"),
    path('reference/', views.ReferenceView, name="reference"),
    path('searchRef/', views.SearchRefView, name="searchRef"),
    path('personalities/', views.PersonalityView, name="personalities"),
    path('logout', views.LogOutView, name="logout"),

    # API routes
    path('intoJSON/', views.IntoJsonView, name="intoJSON"),

    # JSON Files routes
    path('createJSON', views.CreateJSONView, name="createJSON"),

    #  to work on below
    path('topicJSON/', views.TopicJSONView, name="topicJSON"),
    path('bookAdd/', views.BookAddView, name="bookAdd"),
    path('bookSectOption/', views.BookSectOptionView, name="bookSectOption"),
    # path('getTopic/', views.GetTopicView, name="getTopic"),
    path('personalitySearch/', views.PersonalitySearchView, name="personalitySearch"),
    path('osample', views.OSampleView, name="osample"),
]

