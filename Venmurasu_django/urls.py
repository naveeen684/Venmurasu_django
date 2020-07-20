"""Venmurasu_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from home import api
from rest_framework.urlpatterns import format_suffix_patterns
from home import views


urlpatterns = [
    path('api/words/all', api.WordList.as_view()),
    path('api/words/longest/<int:n>', api.LongestWordList.as_view()),
    path('api/words/most-frequent/<int:n>',
         api.MostFrequentWordList.as_view()),
    path('api/words/smallest/<int:n>', api.SmallestWordList.as_view()),
    path('api/words/least-frequent/<int:n>',
         api.LeastFrequentWordList.as_view()),
    path('api/words/search-with-word/<str:x>',
         api.SearchWithWordList.as_view()),


    path('api/words/word-contains/<str:x>',
         api.WordContainsWordList.as_view()),
    path('api/words/start-with/<str:x>',
         api.StartWithWordList.as_view()),
    path('admin/', admin.site.urls),




    path('', views.HomeView.as_view(), name="home"),
    path('search/<str:x>', views.Search, name="search"),
    path('longest/<int:n>', views.LongestWordList.as_view(), name='Longest Words'),
    path('words/most-frequent/<int:n>',
         views.MostFrequentWordList.as_view(), name="Most Frequent"),
    path('words/smallest/<int:n>',
         views.SmallestWordList.as_view(), name="Smallest Words"),
    path('words/least-frequent/<int:n>',
         views.LeastFrequentWordList.as_view(), name="Least Frequent"),
    path('words/search-with-word/<str:x>',
         views.SearchWithWordList.as_view(), name='Exact Match'),


    path('words/word-contains/<str:x>',
         views.WordContainsWordList.as_view(), name='Word Contains'),
    path('words/start-with/<str:x>',
         views.StartWithWordList.as_view(), name='Starts With'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
