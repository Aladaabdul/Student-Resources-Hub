from django.shortcuts import render
from .models import UserProfile, Department, Course, Resource
from .serializers import UserProfileSerializer, DepartmentSerializer, CourseSerializer, ResourceSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
