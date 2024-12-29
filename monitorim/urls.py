from django.urls import include, path

from . import views
from .views import SensorReadingAPI

urlpatterns = [
    path("", views.Home, name="home"),
    path('a/<str:name>/<int:nums>/', views.Add, name='add_book'),
    path('d', views.Del, name='Deletiet'),
    path('sensors/readings',
         SensorReadingAPI.as_view(), name='sensor_reading_api'),
    # URL for getting a specific sensor reading by sensorName
    path('ss/<str:sensor_name>/',
         views.Get_by_name, name='get_sensor_reading_by_name'),
    path("s", views.Show, name="Show")
]
