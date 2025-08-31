from rest_framework import serializers
from .models import JobPost, Application

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = ['id', 'title', 'company', 'description', 'location', 'created_by', 'created_at']
        read_only_fields = ['created_by', 'created_at']

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'job', 'applicant_name', 'applicant_email', 'cover_note', 'applied_at']
        read_only_fields = ['applied_at']
