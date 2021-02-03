from rest_framework.permissions import BasePermission


class IsPermitted(BasePermission):
    def has_permission(self, request, view):
        return all([request.user, request.user.is_authenticated])