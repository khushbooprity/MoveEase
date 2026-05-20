from django.contrib import admin
from django.urls import path
from users import views
urlpatterns = [
    path('index/', views.index),
    path('index2/', views.index),
    path('index3/', views.index),
    path('index4/', views.index),
]