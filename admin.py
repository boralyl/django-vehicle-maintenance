from django.contrib import admin

from vehicle.models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    pass

    
admin.site.register(Vehicle, VehicleAdmin)
