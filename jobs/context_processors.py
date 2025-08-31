# jobs/context_processors.py

from .models import JobPost

def job_notifications(request):
    """Provide job-related notifications to templates"""
    jobs_count = JobPost.objects.count()
    return {
        'jobs_count': jobs_count
    }


def my_context(request):
    return {
        'site_name': 'Job Board Lite'
    }
