# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementDetailSerializer

# получение датчиков

class SensorsAllView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# создание датчика

class CreateSensorView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# обновление датчика
    
class UpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# добавление измерения

class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer

# получение информации по датчику

class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer