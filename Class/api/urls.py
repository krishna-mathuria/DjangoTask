from django.urls import include
from django.conf.urls import url 
from .views import AddGroup, StudentList,UserList, ResetPassword

urlpatterns = [
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^addgroup/', AddGroup),
    url(r'^students', StudentList.as_view()),
    url(r'allusers', UserList.as_view()),
    url(r'^password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',ResetPassword.as_view())
]