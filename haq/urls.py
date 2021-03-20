from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = "haq"
               
urlpatterns = [
    path('books/', views.BookView, name="books"),
    path('status/', views.StatusView, name="status"),
    path('getStatusBooks/<status_id>/', views.GetStatusBooksView, name="getStatusBooks"),
    path('religions/', views.ReligionView, name="religions"),
    path('getReligiousBooks/<sect_id>', views.GetReligiousBooksView, name="getReligiousBooks"),
    path('need/', views.NeedView, name="need"),
    path('getNeedBooks/<need_id>/', views.GetNeedBooksView, name="getNeedBooks"),
    path('languages/', views.LanguagesView, name="languages"),
    path('getLanguagesBooks/<language_id>/', views.GetLanguagesBooksView, name="getLanguagesBooks"),
    path('categories/', views.CategoriesView, name="categories"),
    path('getCategoriesBooks/<category_id>/', views.GetCategoriesBooksView, name="getCategoriesBooks"),
    path('topics/', views.TopicsView, name="topics"),
    # path('getTopic/<topic_id>/', views.GetTopicView, name="getTopic"),
    url(r'^getTopic/(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),
    path('reference/', views.ReferenceView, name="reference"),
    path('personalities/', views.PersonalityView, name="personalities"),
    path('getPersonRef/<person_id>/', views.GetPersonRefView, name="getPersonRef"),


    path('', views.IndexView, name="index"),
    path('index/', views.IndexView, name="index"),
    path('about/', views.AboutView, name="about"),
    path('logout', views.LogOutView, name="logout"),

    # JSON Files routes
    path('createJSON', views.CreateJSONView, name="createJSON"),

    #  to work on below
    path('bookAdd/', views.BookAddView, name="bookAdd"),
    path('bookSectOption/', views.BookSectOptionView, name="bookSectOption"),

    #  other ways to write route
    # path('getTopic/', views.GetTopicView, name="getTopic"),
    # url(r'^getPersonRef/(?P<person_id>[0-9]+)/$', views.GetPersonRefView, name="getPersonRef"),
    # url(r'^getTopic/(?P<topic_id>[0-9]+)/$', views.GetTopicView, name="getTopic"),
    # url(r'^getCategoriesBooks/(?P<category_id>[0-9]+)/$', views.GetCategoriesBooksView, name="getCategoriesBooks"),
    # path(r'^getCategoriesBooks/(?P<category_id>\d+)/$', views.GetCategoriesBooksView, name="getCategoriesBooks"),
    # url(r'^getStatusBooks/(?P<status_id>[0-9]+)/$', views.GetStatusBooksView, name="getStatusBooks"),
    # url(r'^getReligiousBooks/(?P<sect_id>[0-9]+)/$', views.GetReligiousBooksView, name="getReligiousBooks"),
    # url(r'^getNeedBooks/(?P<need_id>[0-9]+)/$', views.GetNeedBooksView, name="getNeedBooks"),
    # url(r'getLanguagesBooks/(?P<language_id>[0-9]+)/$', views.GetLanguagesBooksView, name="getLanguagesBooks"),
    # url(r'^getTopic/(?P<topic_id>\d+)/', views.GetTopicView, name="getTopic"),
    # path(r'getPersonRef/<int:person_id>/', views.GetPersonRefView, name="getPersonRef"),
    
]


