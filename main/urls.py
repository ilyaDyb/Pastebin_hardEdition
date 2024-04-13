from django.urls import path

from main import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
]
