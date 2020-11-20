from django.db import models

# Create your models here.
class Station(models.Model):
    # имя
    name=models.CharField(max_length=250)
    # долгота
    latitude=models.FloatField()
    # ширина
    longitude=models.FloatField()
    # маршруты
    routes = models.ManyToManyField('Route', related_name="stations")

    def __str__(self):
        return self.name

class Route(models.Model):
    # имя
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'Маршрут: {self.name}'
        #return self.name
