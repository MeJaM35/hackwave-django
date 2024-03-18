from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.shortcuts import render, redirect



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
                    return redirect('login_url')
                else:
                    messages.error(request, 'Username is already in use.')
            else:
                messages.error(request, 'Username is already taken.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'core/register.html')



class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    gh_username = models.CharField(max_length=100, unique=True)
    college = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length= 15, default="Year")
    dept = models.CharField(max_length=20, default="Department" )
    activated = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']



DOMAINS = (
     ('Sustainibility', 'Sustainibility'),
     ('Intelligent Automation', 'Intelligent Automation')

)
class Team(models.Model):
    team_id = models.BigAutoField(primary_key=True, default=1000)
    name = models.CharField(max_length=500, null=True)
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lead')
    mem2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mem2', null=True)
    mem3 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='mem3')
    mem3 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='mem4')
    domain = models.CharField(max_length=500, choices = DOMAINS)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        if not self.slug:  # Check if slug is already set
            self.slug = slugify(f"{self.name}-{self.team_id}")
        super(Team, self).save(*args, **kwargs)

# Create your models here.
