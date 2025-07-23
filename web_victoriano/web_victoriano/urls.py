
from django.contrib import admin
from django.urls import path
from web_victoriano.views import saludo


urlpatterns = [
    path('admin/', admin.site.urls),

    path('victoriano/', saludo)

]



