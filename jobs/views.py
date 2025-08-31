from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import JobPost, Application, JobNotification
from django.views.decorators.csrf import csrf_exempt
import json

# Home page - latest 5 jobs
def home(request):
    jobs = JobPost.objects.all().order_by('-created_at')[:5]
    return render(request, 'jobs/home.html', {'jobs': jobs})

# List all jobs
def job_list(request):
    jobs = JobPost.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# Job details
def job_detail(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    applicants = job.applications.all() if job.created_by == request.user else None
    return render(request, 'jobs/job_detail.html', {'job': job, 'applicants': applicants})

# Post a new job (web form)
@login_required
def post_job(request):
    if request.method == 'POST':
        JobPost.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            company=request.POST['company'],
            location=request.POST['location'],
            created_by=request.user
        )
        return redirect('job_list')
    return render(request, 'jobs/post_job.html')

# Apply to a job (web form)
@login_required
def apply_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    if request.method == 'POST':
        Application.objects.create(
            job=job,
            applicant=request.user,
            cover_note=request.POST['cover_note']
        )
        return redirect('job_list')
    return render(request, 'jobs/apply_job.html', {'job': job})

# Job notifications context processor
def job_notifications(request):
    if request.user.is_authenticated:
        notifications = JobNotification.objects.filter(
            job__created_by=request.user, read=False
        ).order_by('-created_at')
        return {'job_notifications': notifications}
    return {'job_notifications': []}

# Mark notifications as read
@login_required
def mark_notifications_read(request):
    JobNotification.objects.filter(
        job__created_by=request.user, read=False
    ).update(read=True)
    return HttpResponse('ok')

# ----------------- API ENDPOINTS -----------------

# Post a job via API
@csrf_exempt
@login_required
def api_post_job(request):
    if request.method == "POST":
        data = json.loads(request.body)
        job = JobPost.objects.create(
            title=data['title'],
            company=data['company'],
            location=data['location'],
            description=data['description'],
            created_by=request.user
        )
        return JsonResponse({'id': job.id, 'message': 'Job posted successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Apply to a job via API
@csrf_exempt
@login_required
def api_apply_job(request):
    if request.method == "POST":
        data = json.loads(request.body)
        job = get_object_or_404(JobPost, id=data['job_id'])
        Application.objects.create(
            job=job,
            applicant=request.user,
            cover_note=data['cover_note']
        )
        return JsonResponse({'message': 'Application submitted successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
