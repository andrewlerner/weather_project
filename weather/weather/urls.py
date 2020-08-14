from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_weather/', include('get_weather.urls')),
    path('', RedirectView.as_view(url='get_weather/', permanent=True)),
]