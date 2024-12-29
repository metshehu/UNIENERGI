from django.db import models

# Create your models here.


class Test(models.Model):
    text = models.CharField(max_length=100)
    nums = models.FloatField()
    other= models.BooleanField(default=True)
class SensorReading(models.Model):
    sensorName=models.CharField(max_length=255)
    value = models.FloatField()
    unit = models.CharField(max_length=5)
    timestamp = models.DateTimeField()
    location = models.CharField(max_length=255)


