from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Anyone can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class StationOwnerCanEditPermission(SafeMethodsOnlyPermission):
    """Only the owner can push new data"""
    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            can_edit = True
        else:
            can_edit = request.user == obj.observation.author
        return (can_edit or
                super(StationOwnerCanEditPermission,
                      self).has_object_permission(request, view, obj))