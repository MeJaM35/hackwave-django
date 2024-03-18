from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify









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
