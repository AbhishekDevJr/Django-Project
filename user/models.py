from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.IntegerField(null = False, blank = False)
    phone_number = models.CharField(max_length = 15, null = False, blank = False)
    company = models.CharField(max_length = 100, null = False, blank = False)
    role = models.CharField(max_length = 50, null = False, blank = False)
    
    def __str__(self):
        return f"{self.user.email}"