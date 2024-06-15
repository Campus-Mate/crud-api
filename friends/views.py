# friends/views.py

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import FriendRequest, Profile

@login_required
def send_friend_request(request, user_id):
    if request.method == 'POST':
        to_user = get_object_or_404(User, id=user_id)
        from_user = request.user
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            return JsonResponse({'status': 'already_sent'})
        FriendRequest.objects.create(from_user=from_user, to_user=to_user)
        return JsonResponse({'status': 'request_sent'})
    return JsonResponse({'status': 'bad_request'}, status=400)

@login_required
def accept_friend_request(request, request_id):
    if request.method == 'POST':
        friend_request = get_object_or_404(FriendRequest, id=request_id)
        if friend_request.to_user == request.user:
            friend_request.accepted = True
            friend_request.save()
            request.user.profile.friends.add(friend_request.from_user.profile)
            friend_request.from_user.profile.friends.add(request.user.profile)
            return JsonResponse({'status': 'request_accepted'})
    return JsonResponse({'status': 'bad_request'}, status=400)

@login_required
def delete_friend(request, user_id):
    user_to_remove = get_object_or_404(User, id=user_id)
    request.user.profile.friends.remove(user_to_remove.profile)
    user_to_remove.profile.friends.remove(request.user.profile)
    return redirect('profile', user_id=request.user.id)

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    friend_requests = user.received_requests.filter(accepted=False)
    return render(request, 'profile.html', {'user': user, 'friend_requests': friend_requests})
