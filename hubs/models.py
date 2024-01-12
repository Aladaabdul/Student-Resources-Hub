from django.db import models
from django.conf import settings
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)

class Course(models.Model):
    name = models.IntegerField()
    course_code = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='hubs/files')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    uploaded_at = models.DateField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)