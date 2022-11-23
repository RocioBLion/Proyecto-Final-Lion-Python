from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("cellphone/", include("cellphone.urls")),
    path("accessorie/", include("accessorie.urls")),
    path("computer/", include("computer.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]   