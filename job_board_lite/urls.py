from django.contrib import admin
from django.urls import path, include
from jobs import views   # ✅ import views from your jobs app

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("jobs/", include("jobs.urls")),
    path("", views.home, name="home"),   # ✅ now views is defined
]
