from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotFound

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

        if not task:
            raise NotFound("Task not found.")
        return next(iter(task), None)

    def get_queryset(self):
        return self.request.user.tasks.all()

    def perform_destroy(self, instance):
        if instance is None or instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        instance.delete()
