from django.urls import path

from .views import SensorView, MeasurementView, SensorChange

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>', SensorChange.as_view()),
]
