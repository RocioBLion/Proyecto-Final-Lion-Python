from django.urls import path

from accessorie import views 

app_name = "accessorie"
urlpatterns = [
    path("accessories", view=views.accessories, name="accessorie-list"),
    path("accessorie/add", view=views.create_accessories, name="accessorie-add"),  
]