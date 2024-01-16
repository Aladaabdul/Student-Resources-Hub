from django.shortcuts import render
from .models import UserProfile, Department, Course
from .serializers import UserProfileSerializer, DepartmentSerializer, CourseSerializer
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
