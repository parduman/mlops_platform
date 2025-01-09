# deployments/views.py
from django.shortcuts import render, redirect
from .forms import DeploymentForm

def create_deployment(request):
    if request.method == 'POST':
        form = DeploymentForm(request.POST)
        if form.is_valid():
            deployment = form.save(commit=False)
            cluster = deployment.cluster
            resources = cluster.available_resources
            if (deployment.ram_required <= resources['ram'] and
                deployment.cpu_required <= resources['cpu'] and
                deployment.gpu_required <= resources['gpu']):
                deployment.status = 'scheduled'
                deployment.save()
                # Trigger deployment task
            else:
                deployment.status = 'queued'
                deployment.save()
                # Add to scheduling queue
            return redirect('deployment_list')
    else:
        form = DeploymentForm()
    return render(request, 'create_deployment.html', {'form': form})

# scheduling.py
def schedule_deployments(deployments):
    return sorted(deployments, key=lambda d: d.priority, reverse=True)
