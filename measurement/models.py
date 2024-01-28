from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    temperature = models.IntegerField()
    date_time = models.DateTimeField()
