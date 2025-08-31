from django.urls import path
from . import views, api_views

urlpatterns = [
    # Web routes
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('post/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('notifications/read/', views.mark_notifications_read, name='mark-notifications-read'),

    # API routes (class-based views)
    path('api/jobs/', api_views.JobListAPI.as_view(), name='api_job_list'),
    path('api/jobs/<int:id>/', api_views.JobDetailAPI.as_view(), name='api_job_detail'),
    path('api/jobs/post/', api_views.PostJobAPI.as_view(), name='api_post_job'),
    path('api/jobs/apply/', api_views.ApplyJobAPI.as_view(), name='api_apply_job'),
]