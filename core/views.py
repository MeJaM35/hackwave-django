from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User



def register_user(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gh_username = request.POST.get('gh_username')
        college = request.POST.get('college')
        year = request.POST.get('year')
        dept = request.POST.get('dept')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password == password_confirmation:
            if not User.objects.filter(username=email).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create(
                        username = email,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone=phone,
                        gh_username=gh_username,
                        college=college,
                        year=year,
                        dept=dept,
                        password=make_password(password),
                        activated=False  # Set to False by default
                    )
                    user.save()
                    # Redirect to login page after successful registration
                else:
                    messages.error(request, 'Username is already in use.')
            else:
                messages.error(request, 'Username is already taken.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'core/register.html')


def index(request):
    return HttpResponse('Site setup')

# Create your views here.
