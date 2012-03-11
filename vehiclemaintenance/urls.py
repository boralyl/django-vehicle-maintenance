from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, TemplateView

from vehiclemaintenance.models import MaintenanceItem
from vehiclemaintenance.views import HistoryList, VehicleList
from vehiclemaintenance.views import OustandingMaintenanceItemsList


urlpatterns = patterns('vehiclemaintenance.views',
    url(r'^$', login_required(TemplateView.as_view(
        template_name="index.html"
        )),
        name="vm-index"),
    url(r'^history/$', login_required(HistoryList.as_view()), name="vm-history"),
    url(r'^item/(?P<pk>[\d]+)/$', DetailView.as_view(
        model=MaintenanceItem,
        template_name="vehiclemaintenance/maintenance_item_details.html"),
        name="vm-maintenance-item-details"),
    url(r'^item/(?P<item_id>[\d]+)/check/$', 'item_check', name="vm-item-check"),
    url(r'^outstanding', login_required(OustandingMaintenanceItemsList.as_view()),
        name="vm-outstanding-items"),
    url(r'^vehicles/$', login_required(VehicleList.as_view()), name="vm-vehicles"),
    url(r'^vehicle/add/$', 'add_edit_vehicle', name="vm-add-vehicle"),
    url(r'^vehicle/edit/(?P<vehicle_id>[\d]+)/$', 'add_edit_vehicle', 
        name="vm-edit-vehicle"),
    url(r'^vehicle/delete/(?P<vehicle_id>[\d]+)/$', 'delete_vehicle', 
        name="vm-delete-vehicle"),
)
