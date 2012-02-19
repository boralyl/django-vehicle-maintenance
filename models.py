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

        
class Occurrence(models.Model):
    """
    Store occurrence options
    """
    name = models.CharField(max_length=50)
    num_days = models.PositiveSmallIntegerField(verbose_name="Number of Days")
    
    def __unicode__(self):
        return self.name
        
        
class MaintenanceItem(models.Model):
    """
    A generic table for entering maintenance items for your vehicle
    """
    name = models.CharField(max_length=75)
    procedure = models.TextField()
    check_occurrence = models.ForeignKey(Occurrence)
    help_videos = models.ManyToManyField("MaintenanceItemVideo", blank=True)
    
    def __unicode__(self):
        return self.name

        
class MaintenanceItemVideo(models.Model):
    """
    Stores videos helpful to a maintenance item
    """
    title = models.CharField(max_length=75)
    embed_code = models.TextField()
    url = models.URLField()

    def __unicode__(self):
        return self.title

        
class MaintenanceItemCheck(models.Model):
    """
    Store recors for when a maintenance item is checked
    """
    vehicle = models.ForeignKey(Vehicle)
    maintenance_item = models.ForeignKey(MaintenanceItem)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    is_passable = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.date, self.maintenance_item.name)
    