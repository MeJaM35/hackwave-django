from django.db import models
from django.contrib.auth.models import AbstractUser


class College(models.Model):
    name = models.CharField(max_length=50, null=True)
    code = models.IntegerField(null=False, unique=True, primary_key=True)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(null=True, unique=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    ghlink = models.URLField()
    college = models.ForeignKey(College, on_delete=models.CASCADE)
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
    name = models.CharField(max_length=500, null=True)
    lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lead')
    mem2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mem2', null=True)
    mem3 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='mem3')
    mem3 = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='mem4')
    domain = models.CharField(max_length=500, choices = DOMAINS)

# Create your models here.
