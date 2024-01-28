from django.urls import path

from .views import sensors, measurements

urlpatterns = [
    path('sensors/', sensors),
    path('measurements/', measurements),
]
