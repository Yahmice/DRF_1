# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorView(APIView):
    def get(self, request):
        sensor = Sensor.objects.all()
        ser = SensorDetailSerializer(sensor, many=True)
        return Response(ser.data)

    def post(self, request):



class MeasurementView(APIView):
    def get(self, request):
        measurement = Measurement.objects.all()
        ser = MeasurementSerializer(measurement, many=True)
        return Response(ser.data)

    def post(self, request):
        pass


class SensorsRetrieve(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

# @api_view(['GET'])
# def sensors(request):
#     sensor = Sensor.objects.all()
#     ser = SensorDetailSerializer(sensor, many=True)
#     return Response(ser.data)


# @api_view(['GET', 'POST'])
# def measurements(request):
#     if request.method == 'GET':
#         measurement = Measurement.objects.all()
#         ser = MeasurementSerializer(measurement, many=True)
#         return Response(ser.data)
#     if request.method == 'POST':
#         pass
