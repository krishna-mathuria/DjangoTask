from django.urls import include
from django.conf.urls import url 
from .views import AddGroup, StudentList,UserList, ResetPassword


urlpatterns = [
    url(r'^auth/', include('djoser.urls')),                                                     #authentication urls
    url(r'^auth/', include('djoser.urls.jwt')),                                                 #JWT Token urls
    url(r'^addgroup/', AddGroup),                                                               #add the user to the specified group
    url(r'^students', StudentList.as_view()),                                                   #List of all students for the teachers
    url(r'allusers', UserList.as_view()),                                                       #List of all the users for Super-admins
    url(r'^password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',ResetPassword.as_view()) #The url that would be mailed to users opting to reset the password
]

"""
Some important djoser urls
To create a user:                           /users/
To update the authenticated user:           /users/me/
To set a new password for existing users:   /users/set_password/
To receive email with reset password link:  /users/reset_password/
To Login/generate JWT:                      /jwt/create/
To refresh the JWT:                         /jwt/refresh/
To Verify the JWT:                          /jwt/verify/

"""