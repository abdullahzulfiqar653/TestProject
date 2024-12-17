from django.urls import path, include
from apis.views import TaskListCreateView, TaskRetrieveUpdateDestroyView

from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task_list_create"),
    path(
        "tasks/<int:pk>",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task_retrieve_update_destry",
    ),
    path("auth/", include("rest_framework.urls")),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
