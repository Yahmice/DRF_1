from django.urls import path

from .views import SensorView, MeasurementView, SensorsRetrieve

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensor view/<pk>', SensorsRetrieve.as_view()),
]
