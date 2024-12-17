from django.db import connection
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apis.models import Task
from apis.serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks.all().order_by("-created_at")[:4]


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        task_id = self.kwargs.get("pk")
        user_id = self.request.user.id
        query = "SELECT * FROM apis_task WHERE user_id = %s AND id = %s"
        task = Task.objects.raw(query, [user_id, task_id])
        return next(iter(task), None)

    def get_queryset(self):
        return self.request.user.tasks.all()
