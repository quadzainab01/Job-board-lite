from rest_framework import generics, permissions
from .models import JobPost, Application
from .serializers import JobPostSerializer, ApplicationSerializer

# List all jobs
class JobListAPI(generics.ListAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated]

# Job details
class JobDetailAPI(generics.RetrieveAPIView):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

# Create a new job
class PostJobAPI(generics.CreateAPIView):
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Apply to a job
class ApplyJobAPI(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
