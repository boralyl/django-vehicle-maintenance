from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, TemplateView

from vehiclemaintenance.models import MaintenanceItem
from vehiclemaintenance.views import OustandingMaintenanceItemsList


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(
        template_name="index.html"
        ),
        name="index"),
    url(r'^item/(?P<pk>[\d]+)/$', DetailView.as_view(
        model=MaintenanceItem,
        template_name="vehiclemaintenance/maintenance_item_details.html"),
        name="maintenance-item-details"),
    url(r'^outstanding', OustandingMaintenanceItemsList.as_view(),
        name="outstanding-maintenance-items"),
)
