from django.shortcuts import render
from rest_framework.response import Response
from .models import UserProfile, Department, Course, Resource, Comment
from .serializers import UserProfileSerializer, DepartmentSerializer, CourseSerializer, ResourceSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import DefaultPagination
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    def me(self, request):
        (user, created) = UserProfile.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = UserProfileSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']


class ResourceViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title']


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
