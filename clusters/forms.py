from django import forms
from .models import Cluster

class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['name', 'ram', 'cpu', 'gpu']