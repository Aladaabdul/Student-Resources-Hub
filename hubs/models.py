from django.db import models
from django.conf import settings
from django.contrib import admin
# Create your models here.

class UserProfile(models.Model):
    USER_ROLE_CHOICES = [
        ('staff', 'Staff'),
        ('student', 'Student'),
    ]

    user_name = models.CharField(max_length=255)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)

    def is_staff(self):
        return self.role == 'staff'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    @admin.display(ordering='user__first_name') # Allow use to by name in Admin page (Allow ordering by firstname)
    def first_name(self):
         return self.user.first_name
    
    @admin.display(ordering="user__last_name")
    def last_name(self):
         return self.user.last_name
    
    class Meta:
         ordering = ['user__first_name', 'user__last_name']

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='hubs/files')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    uploaded_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    uploaded_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    comment = models.TextField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    commented_at = models.DateField(auto_now_add=True)