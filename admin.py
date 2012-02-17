from django.contrib import admin

from vehicle.models import MaintenanceItem, MaintenanceItemVideo, Occurrence, Vehicle


class MaintenanceItemAdmin(admin.ModelAdmin):
    pass

    
class MaintenanceItemVideoAdmin(admin.ModelAdmin):
    pass
    
    
class OccurrenceAdmin(admin.ModelAdmin):
    pass


class VehicleAdmin(admin.ModelAdmin):
    pass

    
admin.site.register(MaintenanceItem, MaintenanceItemAdmin)
admin.site.register(MaintenanceItemVideo, MaintenanceItemVideoAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Vehicle, VehicleAdmin)
