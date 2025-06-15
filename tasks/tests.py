from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task


class TaskAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='abcdef')
        self.client.login(username='test_user', password='abcdef')
        self.task = Task.objects.create(
            title='Test Self Task',
            description='Test Self Task Description',
            due_date='2025-06-14',
            status='in-progress',
            creator=self.user,
        )

    def test_create_task(self):
        url = reverse('task-create')
        data = {
            'title': 'Test Create Task',
            'description': 'Task Create Description',
            'due_date': '2025-06-14',
            'status': 'pending',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.response_expected_check(response.data, data)

    def test_list_tasks(self):
        url = reverse('task-get-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0]['title'], self.task.title)
        self.assertEqual(response.data[0]['description'], self.task.description)
        self.assertEqual(response.data[0]['due_date'], self.task.due_date)
        self.assertEqual(response.data[0]['status'], self.task.status)

    def test_update_task(self):
        url = reverse('task-update', args=[self.task.id])
        data = {
            'title': 'Test Update Task',
            'description': 'Task Update Description',
            'due_date': '2025-06-14',
            'status': 'completed',
        }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.response_expected_check(response.data, data)

    def test_delete_task(self):
        url = reverse('task-delete', args=[self.task.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def response_expected_check(self, response_data, expected_data):
        for field in ['title', 'description', 'due_date', 'status']:
            self.assertEqual(response_data[field], expected_data[field])


