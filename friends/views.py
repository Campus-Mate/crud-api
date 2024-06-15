# friends/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FriendRequest

@login_required
def send_friend_request(request, user_id):
    to_user = get_object_or_404(User, id=user_id)
    from_user = request.user
    FriendRequest.objects.create(from_user=from_user, to_user=to_user)
    return redirect('profile', user_id=user_id)

@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.to_user == request.user:
        friend_request.accepted = True
        friend_request.save()
    return redirect('profile', user_id=friend_request.from_user.id)

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    friend_requests = user.received_requests.filter(accepted=False)
    return render(request, 'profile.html', {'user': user, 'friend_requests': friend_requests})
