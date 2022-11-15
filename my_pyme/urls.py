from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("cellphone/", include("cellphone.urls")),
    path("accessorie/", include("accessorie.urls")),
    path("computer/", include("computer.urls")),
]

