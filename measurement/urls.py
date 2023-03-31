from django.urls import path
from .views import SensorsAllView, SensorView, CreateSensorView, UpdateSensorView, CreateMeasurementView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsAllView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/update/<pk>/', UpdateSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
]
