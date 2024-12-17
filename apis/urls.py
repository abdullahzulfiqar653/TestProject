from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from apis.views import (
    UserCreateAPIView,
    TaskListCreateView,
    TaskRetrieveUpdateDestroyView,
)


urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task_list_create"),
    path(
        "tasks/<int:pk>/",
        TaskRetrieveUpdateDestroyView.as_view(),
        name="task_retrieve_update_destry",
    ),
    path("auth/", include("rest_framework.urls")),
    path("auth/users/", UserCreateAPIView.as_view()),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
