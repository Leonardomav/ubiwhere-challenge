from rest_framework import permissions


# file for custom permissions.

class IsAuthorOrStaff(permissions.BasePermission):
    """
    Description:
        Check if the user making the request is the author of the object or is staff;
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        elif obj.author == request.user:
            return True

        # Checks if request has a user associated and is staff.
        elif bool(request.user and request.user.is_staff):
            return True
