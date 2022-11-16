from django.urls import path

from computer import views

app_name = "computer"
urlpatterns = [
    path("computers", view=views.computers, name="computer-list"),
    path("computer/add", view=views.create_computers, name="computer-add"),
    ]