# friends/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('send_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('delete_friend/<int:user_id>/', views.delete_friend, name='delete_friend'),
]
