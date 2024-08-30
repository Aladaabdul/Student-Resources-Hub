from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user and request.user.is_authenticated:
            user_profile = getattr(request.user, 'userprofile', None)
            if user_profile and user_profile.is_staff():
                return True
        
        return False