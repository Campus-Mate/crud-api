from django.contrib import admin
from django.urls import path, include
from student.api import StudentList, StudentDetail
from board.api import BoardList, BoardDetail

urlpatterns = [
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list', StudentList.as_view(), name='student_list'),
    path('api/student_list/<int:student_id>', StudentDetail.as_view(), name='student_detail'),
    path('api/board_list', BoardList.as_view(), name='board_list'),
    path('api/board_list', BoardList.as_view(), name='board_list'),
    path('api/board_list/<int:board_id>', BoardDetail.as_view(), name='board_detail'),
    path('admin/', admin.site.urls),
    path('friends/', include('friends.urls')),
]
