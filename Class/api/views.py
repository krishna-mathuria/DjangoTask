from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .decorators import authenticate_users
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
import requests
from .serializer import UserSerializer, StudentSerializer
# Create your views here.

User=get_user_model()

@api_view(['POST'])
def AddGroup(request):
    if request.method == 'POST':
        my_group = Group.objects.get(name=request.data['group']) 
        my_group.user_set.add(request.user)
        return Response("Successfully added")



@method_decorator(authenticate_users(allowed_roles=["Teacher"]), name="get")
class StudentList(generics.ListAPIView):
    serializer_class=StudentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.filter(groups__name='Student')


@method_decorator(authenticate_users(allowed_roles=["Super-admin"]), name="get")
class UserList(generics.ListAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]
    queryset = User.objects.all()


class ResetPassword(APIView):

    def post(self, request, uid, token):
        try:
            new_password = request.data['new_password']
            re_new_password = request.data['re_new_password']
            protocol = 'https://' if request.is_secure() else 'http://'
            web_url = protocol + request.get_host()
            post_url = web_url + "/auth/users/reset_password_confirm/"
            post_data = {'uid': uid, 'token': token,'new_password':new_password,'re_new_password':re_new_password}
            result = requests.post(post_url, data = post_data)
            return Response(result)
        except Exception as e:
            return Response(str(e))
