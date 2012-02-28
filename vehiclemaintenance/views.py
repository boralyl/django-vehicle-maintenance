from django.shortcuts import render
from django.views.generic import ListView

from vehiclemaintenance.models import MaintenanceItem


class OustandingMaintenanceItemsList(ListView):
    """
    Lists outstanding mainetance tasks for a user
    """
    context_object_name = "maintenance_items"
    queryset = MaintenanceItem.objects.get_outstanding_items()
    template_name = "vehiclemaintenance/outstanding_items_list.html"

