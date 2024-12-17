from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Selteq task",
        default_version="v1",
        description="Selteq Task Project",
    ),
    public=True,
    permission_classes=[],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/", include("apis.urls")),
]
