from django.test import TestCase
from .models import Cluster
from django.urls import reverse
from .forms import ClusterForm

class ClusterModelTest(TestCase):
    def setUp(self):
        self.cluster = Cluster.objects.create(name='Test Cluster', ram=16, cpu=8, gpu=2)

    def test_cluster_creation(self):
        self.assertEqual(self.cluster.name, 'Test Cluster')
        self.assertEqual(self.cluster.ram, 16)
        self.assertEqual(self.cluster.cpu, 8)
        self.assertEqual(self.cluster.gpu, 2)

class ClusterViewTest(TestCase):
    def test_cluster_list_view(self):
        response = self.client.get(reverse('cluster_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clusters/cluster_list.html')

class ClusterFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Test Cluster', 'ram': 16, 'cpu': 8, 'gpu': 2}
        form = ClusterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'ram': 16, 'cpu': 8, 'gpu': 2}
        form = ClusterForm(data=data)
        self.assertFalse(form.is_valid())