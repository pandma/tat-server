from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/page", include("Apps.Pages.urls")),
    path("api/subpages", include("Apps.Subpages.urls")),
    path("api/tasks", include("Apps.Tasks.urls")),
]
