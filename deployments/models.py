# deployments/models.py
from django.db import models
from clusters.models import Cluster

class Deployment(models.Model):
    cluster = models.ForeignKey(Cluster, related_name='deployments', on_delete=models.CASCADE)
    docker_image = models.CharField(max_length=255)
    ram_required = models.FloatField()
    cpu_required = models.FloatField()
    gpu_required = models.FloatField()
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)
