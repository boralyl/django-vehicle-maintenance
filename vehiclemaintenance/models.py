from datetime import date, timedelta

from django.contrib.auth.models import User
from django.db import models


class Vehicle(models.Model):
    """
    Defines a vehicle, going to keep it relatively generic
    """
    user = models.ForeignKey(User)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=75)
    year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('-year', 'make', 'model')
    
    def __unicode__(self):
        return " ".join((str(self.year), self.make, self.model))


class Occurrence(models.Model):
    """
    Store occurrence options
    """
    name = models.CharField(max_length=50)
    num_days = models.PositiveSmallIntegerField(verbose_name="Number of Days")

    class Meta:
        ordering = ('num_days', 'name')

    def __unicode__(self):
        return self.name


class MaintenanceItemManager(models.Manager):
    """
    Manager fuctions for the MaintenanceItem model
    """

    def get_outstanding_items(self, user):
        """
        Returns a list of outstanding maintenance items
        """
        return [i for i in MaintenanceItem.objects.all()
            if not i.maintenanceitemcheck_set.filter(user=user,
                date__gte=(
                    date.today() - timedelta(days=i.check_occurrence.num_days)))]
    
    def get_upcoming_items(self, user, num_days):
        """
        Returns a list of items upcoming in `num_days` days based on the last 
        check date.
        """
        return [i for i in MaintenanceItem.objects.all()
            for c in i.maintenanceitemcheck_set.filter(user=user)[:1]
                if (date.today() - c.date).days + num_days >= i.check_occurrence.num_days]


class MaintenanceItem(models.Model):
    """
    A generic table for entering maintenance items for your vehicle
    """
    name = models.CharField(max_length=75)
    procedure = models.TextField()
    check_occurrence = models.ForeignKey(Occurrence)
    help_videos = models.ManyToManyField("MaintenanceItemVideo", blank=True)

    objects = MaintenanceItemManager()

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
    user = models.ForeignKey(User)
    vehicle = models.ForeignKey(Vehicle)
    maintenance_item = models.ForeignKey(MaintenanceItem)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()
    is_passable = models.BooleanField(default=True)

    class Meta:
        ordering = ('-date', )

    def __unicode__(self):
        return "%s - %s" % (self.date, self.maintenance_item.name)
