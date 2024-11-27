from django.db import models

from base64 import encode, decode

class Map(models.Model):
    name = models.CharField(max_length=50)
    is_vanilla = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class Guess(models.Model):
    picture = models.BinaryField()
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.map) + " - " + str(self.x_coord) + ":" + str(self.y_coord)

class User(models.Model):
    #TODO User model
    pass