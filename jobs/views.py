from django.shortcuts import render, redirect

def job_list(request):
    return render(request, 'jobs/job_list.html')

def job_detail(request, job_id):
    return render(request, 'jobs/job_detail.html')

def post_job(request):
    return render(request, 'jobs/post_job.html')

def apply_job(request, job_id):
    return render(request, 'jobs/apply_job.html')
