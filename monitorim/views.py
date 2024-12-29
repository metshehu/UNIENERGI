from django.shortcuts import HttpResponse, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SensorReading, Test
from .serializers import SensorReadingSerializer


def Home(request):
    return HttpResponse("<h1>hello world</h1>")


def Add(request, name, nums):
    b1 = Test.objects.create(text=name, nums=nums, other=False)
    return HttpResponse("add it doen ")


def Del(request):
    records = SensorReading.objects.all()
    records.delete()
    return HttpResponse("done")


def Show(reuqest):
    a = SensorReading.objects.all()
    text = ""
    for i in a:
        text += f"|{i.sensorName}|"
    text += "------"
    text += str(len(a))
    return HttpResponse(text)


def Get_by_name(request, sensor_name):
    sensor_reading = SensorReading.objects.get(sensorName=sensor_name)
    return HttpResponse(sensor_reading)


class SensorReadingAPI(APIView):
    def post(self, request):
        # Use sensor_id as needed, it comes from the URL
        serializer = SensorReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data saved successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        records = SensorReading.objects.all()
        records.delete()
        return Response({"message": "Data Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request):

        # Fetch all sensor readings
        sensor_readings = SensorReading.objects.all()
        serializer = SensorReadingSerializer(sensor_readings, many=True)
        return Response({"message": "All sensor readings", "data": serializer.data}, status=status.HTTP_200_OK)

    # GET a specific SensorReading by sensorNam
       # return Response({"message": f"this is {serializer.data.get(key="sensorName")}", "data": serializer.data}, status = status.HTTP_200_OK)
