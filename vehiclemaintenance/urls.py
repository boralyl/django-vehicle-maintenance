from django.conf.urls.defaults import patterns, url

from vehicle.views import OustandingMaintenanceItemsList


urlpatterns = patterns('',
    url(r'^outstanding', OustandingMaintenanceItemsList.as_view(),
        name="outstanding-items"),
)
