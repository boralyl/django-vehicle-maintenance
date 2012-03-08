from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, TemplateView

from vehiclemaintenance.models import MaintenanceItem
from vehiclemaintenance.views import HistoryList
from vehiclemaintenance.views import OustandingMaintenanceItemsList


urlpatterns = patterns('vehiclemaintenance.views',
    url(r'^$', TemplateView.as_view(
        template_name="index.html"
        ),
        name="vm-index"),
    url(r'^history/$', HistoryList.as_view(), name="vm-history"),
    url(r'^item/(?P<pk>[\d]+)/$', DetailView.as_view(
        model=MaintenanceItem,
        template_name="vehiclemaintenance/maintenance_item_details.html"),
        name="maintenance-item-details"),
    url(r'^outstanding', OustandingMaintenanceItemsList.as_view(),
        name="vm-outstanding-items"),
)
