from django.conf.urls.defaults import patterns, url

from vehiclemaintenance.views import OustandingMaintenanceItemsList


urlpatterns = patterns('',
    url(r'^outstanding', OustandingMaintenanceItemsList.as_view(),
        name="outstanding-items"),
)
