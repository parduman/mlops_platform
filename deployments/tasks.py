# deployments/tasks.py
from celery import shared_task
from .models import Deployment

@shared_task
def schedule_deployments():
    queued_deployments = Deployment.objects.filter(status='queued').order_by('-priority', 'created_at')
    for deployment in queued_deployments:
        cluster = deployment.cluster
        resources = cluster.available_resources
        if (deployment.ram_required <= resources['ram'] and
            deployment.cpu_required <= resources['cpu']
