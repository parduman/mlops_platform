# clusters/models.py
from django.db import models
from users.models import Organization

class Cluster(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    total_ram = models.FloatField()  # in GB
    total_cpu = models.FloatField()  # in cores
    total_gpu = models.FloatField()  # in units

    @property
    def available_resources(self):
        allocated = self.deployments.aggregate(
            total_ram=models.Sum('ram_required'),
            total_cpu=models.Sum('cpu_required'),
            total_gpu=models.Sum('gpu_required')
        )
        return {
            'ram': self.total_ram - (allocated['total_ram'] or 0),
            'cpu': self.total_cpu - (allocated['total_cpu'] or 0),
            'gpu': self.total_gpu - (allocated['total_gpu'] or 0),
        }
