from django.contrib import admin
from django.urls import path, include

from cellphone.views import create_cellphones
from computer.views import create_computers
from accessorie.views import create_accessories


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("cellphone/", include("cellphone.urls")),
    path("accessorie/", include("accessorie.urls")),
    path("computer/", include("computer.urls")),
   
]   



