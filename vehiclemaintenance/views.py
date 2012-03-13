from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from vehiclemaintenance.forms import ItemCheckForm, VehicleForm
from vehiclemaintenance.models import MaintenanceItem, MaintenanceItemCheck
from vehiclemaintenance.models import Vehicle


class OustandingMaintenanceItemsList(ListView):
    """
    Lists outstanding mainetance tasks for a user
    """
    context_object_name = "maintenance_items"
    template_name = "vehiclemaintenance/outstanding_items_list.html"
    
    def get_queryset(self):
        """
        Only show maintenance items for the logged in user
        """
        return MaintenanceItem.objects.get_outstanding_items(self.request.user)


class HistoryList(ListView):
    """
    Lists history of recent maintenance item checks
    """
    context_object_name = "check_history"
    template_name = "vehiclemaintenance/history_list.html"
    
    def get_queryset(self):
        """
        Only show maintenance items for the logged in user
        """
        return MaintenanceItemCheck.objects.filter(user=self.request.user)
    
    
class UpcomingList(ListView):
    """
    Lists upcoming maintenance items that are due.
    """
    context_object_name = "maintenance_items"
    template_name = "vehiclemaintenance/upcoming_list.html"
    
    def get_queryset(self):
        """
        Only show maintenance items for the logged in user
        """
        return MaintenanceItem.objects.get_upcoming_items(self.request.user,
            num_days=7)

    
class VehicleList(ListView):
    """
    Lists all of a user's vehicles
    """
    context_object_name = "vehicle_list"
    template_name = "vehiclemaintenance/vehicles_list.html"
    
    def get_queryset(self):
        """
        Only show vehicles belonging to the logged in user
        """
        return Vehicle.objects.filter(user=self.request.user)


@login_required
def item_check(request, item_id):
    """
    Allow users to input a maintenance check
    """
    temp_vars = {}
    item = get_object_or_404(MaintenanceItem, pk=item_id)
    vehicles = request.user.vehicle_set.all()
    if not vehicles:
        return redirect("vm-vehicle-add")
    vehicle = vehicles[0]
    instance = MaintenanceItemCheck(user=request.user, maintenance_item=item,
        vehicle=vehicle)
    
    form = ItemCheckForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('vm-maintenance-item-details', args=(item_id, )) + "#history")
        
    temp_vars['form'] = form
        
    return render(request, "vehiclemaintenance/item_check_form.html", temp_vars)

    
@login_required
def add_edit_vehicle(request, vehicle_id=None):
    """
    Allows a user to add/modify a vehicle
    """
    temp_vars = {}
    if vehicle_id:
        instance = get_object_or_404(Vehicle, pk=vehicle_id)
    else:
        instance = Vehicle(user=request.user)
    
    form = VehicleForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect("vm-vehicles")
    
    temp_vars['form'] = form
    
    return render(request, "vehiclemaintenance/add_edit_vehicle_form.html", temp_vars)

    
@login_required
def delete_vehicle(request, vehicle_id):
    """
    Allows a user to delete a vehicle
    """
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if vehicle.user == request.user:
        vehicle.delete()
    return redirect("vm-vehicles")

    
@login_required
def dashboard(request):
    """
    Shows upcoming and outstanding items for a user
    """
    temp_vars = {}
    
    temp_vars['outstanding_items'] = MaintenanceItem.objects.get_outstanding_items(
        request.user)
    temp_vars['upcoming_items'] = MaintenanceItem.objects.get_upcoming_items(
        request.user, num_days=7)
    
    return render(request, "vehiclemaintenance/dashboard.html", temp_vars)
