from django.db import models


class Vehicle(models.Model):
    """
    Defines a vehicle, going to keep it relatively generic
    """
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=75)
    year = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return " ".join((str(self.year), self.make, self.model))
