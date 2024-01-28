# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


@api_view(['GET'])
def sensors(request):
    sensor = Sensor.objects.all()
    ser = SensorSerializer(sensor, many=True)
    return Response(ser.data)


@api_view(['GET'])
def measurements(request):
    measurement = Measurement.objects.all()
    ser = MeasurementSerializer(measurement, many=True)
    return Response(ser.data)
