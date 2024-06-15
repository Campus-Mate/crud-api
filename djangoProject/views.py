# myproject/views.py

from django.shortcuts import redirect

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def home_redirect(request):
    return redirect('/friends/profile/1/')  # 적절한 user_id로 수정
