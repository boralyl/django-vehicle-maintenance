from django import forms
from django.forms.models import ModelForm

from vehiclemaintenance.models import MaintenanceItemCheck, Vehicle


YES_NO = [('1', 'Yes'), ('0', 'No')]


class ItemCheckForm(ModelForm):
    """
    Form for entering maintenance item checks
    """
    is_passable = forms.Field(widget=forms.RadioSelect(choices=YES_NO))
    
    class Meta:
        model = MaintenanceItemCheck
        exclude = ('user', 'maintenance_item')


class VehicleForm(ModelForm):
    """
    Form for adding/editing vehicles
    """
    
    class Meta:
        model = Vehicle
        exclude = ('user', )
