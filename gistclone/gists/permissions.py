from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the gist.
        return obj.owner == request.user

""" class IsGistOwner(permissions.BasePermission):
    #for view permisson
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    #for object level permissions
    def has_object_permission(self, request, view, gist_obj):
        return gist_obj.owner.id == request.user.id """




