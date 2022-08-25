from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkroom),
    path('send',views.send),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
]
