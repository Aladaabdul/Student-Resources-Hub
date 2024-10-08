from rest_framework import serializers
from hubs.models import UserProfile, Department, Course, Resource, Comment

class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only = True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user_id', 'user_name', 'role']

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class CourseSerializer(serializers.ModelSerializer):
    # department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    department = DepartmentSerializer()

    class Meta:
        model = Course
        fields = ['id', 'name', 'course_code', 'department']

    def create(self, validated_data):
        department_data = validated_data.pop('department', None)

        # If department data is provided, create or get the department instance
        if department_data:
            department_instance, created = Department.objects.get_or_create(**department_data)
            validated_data['department'] = department_instance

        return super().create(validated_data)

    def update(self, instance, validated_data):
        department_data = validated_data.pop('department', None)

        # If department data is provided, create or get the department instance
        if department_data:
            department_instance, created = Department.objects.get_or_create(**department_data)
            validated_data['department'] = department_instance

        return super().update(instance, validated_data)

class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'file', 'department', 'course', 'uploaded_by', 'uploaded_at']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment', 'resource', 'commented_by', 'commented_at']