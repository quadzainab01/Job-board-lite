from django.urls import path
from .views import (
    job_list,
    job_detail,
    post_job,
    apply_job,
    mark_notifications_read
)

urlpatterns = [
    path('', job_list, name='job_list'),
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('post/', post_job, name='post_job'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('notifications/read/', mark_notifications_read, name='mark-notifications-read'),
]
