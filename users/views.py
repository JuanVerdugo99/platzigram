"""User views."""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from .models import Profile

@login_required
def update_profile(request):
    """Update a user's profile view."""
    return render(request, 'users/update_profile.html')

def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        passw_confirmation = request.POST['passwd_confirmation']

        if passwd != passw_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']

        profile = Profile(user=user)
        profile.save()

        return redirect('feed')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect('login')