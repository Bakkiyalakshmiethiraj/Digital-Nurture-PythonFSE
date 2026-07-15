from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Enterprise Course Management API",
        default_version='v1',
        description="REST API for Course Management System",
        contact=openapi.Contact(email="admin@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

    authentication_classes=[],
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("courses.urls")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Swagger Documentation
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-ui",
    ),

    # ReDoc Documentation
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc",
    ),
]