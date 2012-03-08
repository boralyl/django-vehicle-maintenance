from django.shortcuts import render
from django.views.generic import ListView

from vehiclemaintenance.models import MaintenanceItem, MaintenanceItemCheck


class OustandingMaintenanceItemsList(ListView):
    """
    Lists outstanding mainetance tasks for a user
    """
    context_object_name = "maintenance_items"
    queryset = MaintenanceItem.objects.get_outstanding_items()
    template_name = "vehiclemaintenance/outstanding_items_list.html"


class HistoryList(ListView):
    """
    Lists history of recent maintenance item checks
    """
    context_object_name = "check_history"
    queryset = MaintenanceItemCheck.objects.all()
    template_name = "vehiclemaintenance/history_list.html"
