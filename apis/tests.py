from apis.models import Task
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client = APIClient()
        self.token = self.get_jwt_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

        self.task_data = {
            "title": "Test Task",
            "duration": 5,
        }
        self.task = Task.objects.create(
            user=self.user, title="Initial Task", duration=7
        )

    def get_jwt_token(self, user):
        url = reverse("token_obtain_pair")
        response = self.client.post(
            url, {"username": user.username, "password": "password"}
        )
        return response.data["access"]

    def test_create_task(self):
        url = reverse("task_list_create")
        response = self.client.post(url, self.task_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # Task count should increase by 1
        self.assertEqual(response.data["title"], self.task_data["title"])
        self.assertEqual(response.data["duration"], self.task_data["duration"])

    def test_get_tasks(self):
        url = reverse("task_list_create")
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one task should be returned

    def test_retrieve_task(self):
        url = reverse(
            "task_retrieve_update_destry", kwargs={"pk": self.task.id}
        )  # Use task's ID for retrieval
        response = self.client.get(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)

    def test_update_task(self):
        url = reverse("task_retrieve_update_destry", kwargs={"pk": self.task.id})
        updated_data = {
            "title": "Updated Task Title",  # Only title is allowed to be updated
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data["title"])

    def test_update_task_invalid_fields(self):
        url = reverse("task_retrieve_update_destry", kwargs={"pk": self.task.id})
        data = {"title": "Updated", "duration": 9}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.task.refresh_from_db()
        self.assertNotEqual(self.task.duration, 9)  # Duration should remain unchanged

    def test_delete_task(self):
        url = reverse("task_retrieve_update_destry", kwargs={"pk": self.task.id})
        response = self.client.delete(url, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)  # Task should be deleted

    def test_delete_task_other_user(self):
        user_2 = User.objects.create_user(username="user_2", password="password")
        task_2 = Task.objects.create(user=user_2, title="Another User Task", duration=5)

        url = reverse("task_retrieve_update_destry", kwargs={"pk": task_2.id})
        response = self.client.delete(url, format="json")

        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND
        )  # Cannot delete task of another user

    def test_get_task_not_found(self):
        url = reverse(
            "task_retrieve_update_destry", kwargs={"pk": 9999}
        )  # Non-existent task ID
        response = self.client.get(url, format="json")

        self.assertEqual(
            response.status_code, status.HTTP_404_NOT_FOUND
        )  # Task should not be found
