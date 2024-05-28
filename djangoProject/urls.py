"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from student.api import StudentList, StudentDetail
from board.api import BoardList, BoardDetail

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path('accounts/', include('accountapp.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list/<int:student_id>', StudentDetail.as_view(), name='student_detail'),
    path('api/board_list', BoardList.as_view(), name='board_list'),
    path('api/board_list', BoardList.as_view(), name='board_list'),
    path('api/board_list/<int:board_id>', BoardDetail.as_view(), name='board_detail'),
    # path('api/auth', views.obtain_auth_token, name='user_auth-create'),
]
