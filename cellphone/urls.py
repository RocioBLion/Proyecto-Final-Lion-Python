from django.urls import path

from cellphone import views

app_name = "cellphone"
urlpatterns = [
    path("cellphones", view=views.cellphones, name="cellphone-list"),
    path("cellphone/add", view=views.create_cellphones, name="cellphone-add"), 
]