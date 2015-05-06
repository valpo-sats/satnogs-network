from rest_framework import permissions


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Anyone can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class StationOwnerCanViewPermission(permissions.BasePermission):
    """Only the owner can view station jobs"""
    def has_object_permission(self, request, view, obj=None):
        if obj is None:
            can_edit = True
        else:
            can_edit = request.user == obj.ground_station.owner
        return can_edit


class StationOwnerCanEditPermission(permissions.BasePermission):
    """Only the owner can edit station jobs"""
    def has_object_permission(self, request, view, obj=None):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj is None:
            can_edit = True
        else:
            can_edit = request.user == obj.ground_station.owner
        return can_edit
