from django.urls import path 
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('users', views.UserProfileViewSet)
router.register('department', views.DepartmentViewSet)
router.register('course', views.CourseViewSet)
router.register('resources', views.ResourceViewSet)


urlpatterns = router.urls