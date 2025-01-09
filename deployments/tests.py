from django.test import TestCase
from .models import Deployment
from .views import schedule_deployments

class SchedulingAlgorithmTest(TestCase):
    def setUp(self):
        self.deployment1 = Deployment(name='Low Priority', priority=1, ram_required=4, cpu_required=2, gpu_required=0)
        self.deployment2 = Deployment(name='High Priority', priority=10, ram_required=8, cpu_required=4, gpu_required=1)

    def test_scheduling_order(self):
        deployments = [self.deployment1, self.deployment2]
        scheduled = schedule_deployments(deployments)
        self.assertEqual(scheduled[0].name, 'High Priority')
        self.assertEqual(scheduled[1].name, 'Low Priority')