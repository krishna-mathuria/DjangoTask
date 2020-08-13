from rest_framework.response import Response
from rest_framework import status

def authenticate_users(allowed_groups=[]):
    """
        decorator to authenticate users to particular model;
        will determine the the group that can access the particular endpoint
    """

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = allowed_groups[0]
            group_list = [group.name for group in request.user.groups.all()]
            if group in group_list:
                return view_func(request, *args, **kwargs)
            else:
                return Response(
                    {"message": ["You are not authorized"]},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        return wrapper_func

    return decorator