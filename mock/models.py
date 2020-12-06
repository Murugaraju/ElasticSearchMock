from django.db import models
class Car(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])