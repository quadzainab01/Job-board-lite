from django.db import models
from django.conf import settings

# Job posting model
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Application model for applying to jobs
class Application(models.Model):
    job = models.ForeignKey(JobPost, related_name='applications', on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_note = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')
    
    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"

# Notification model for job postings
class JobNotification(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.job.title}"
