from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

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



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)