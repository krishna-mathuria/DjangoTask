from rest_framework.response import Response
from rest_framework import status

def authenticate_users(allowed_roles=[]):
    """
        decorator to authenticate users to particular model;
        named _partners becuase it will be mostly app specific
    """

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print("working")
            group = allowed_roles[0]
            # print(request.user)
            # print(group)
            # print(request.user.groups.all())
            # print(request.user)
            group_list = [group.name for group in request.user.groups.all()]
            if group in group_list:
                # print(allowed_roles)
                # print("working")
                return view_func(request, *args, **kwargs)
            else:
                return Response(
                    {"message": ["You are not authorized"]},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        return wrapper_func

    return decorator