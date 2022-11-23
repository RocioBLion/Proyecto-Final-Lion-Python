from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import reverse_lazy

from home import views

app_name = "home"
urlpatterns = [
    path("", view=views.index, name="index"),
    path("search/", views.search, name="search"),
    path('avatar/load', views.avatar_load, name='avatar-load'),
]










