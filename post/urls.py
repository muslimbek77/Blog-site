from django.contrib import admin
from django.urls import path
from .views import PostList, indexview
urlpatterns = [
    path('', indexview, name='index' ),
    path('v/', PostList.as_view()),
]
