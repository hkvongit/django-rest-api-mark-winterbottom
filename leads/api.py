from leads.models import Lead,Project
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer,ProjectSerializer

# Lead Viewset


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = LeadSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer
