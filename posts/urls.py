from django.urls import path
from posts import views


app_name = "posts"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("<str:hash_id>/", views.post_detail, name="post_detail"),

]
