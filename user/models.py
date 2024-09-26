from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    mac_address = models.GenericIPAddressField()
    company = models.CharField(max_length = 100)
    role = models.CharField(max_length = 50)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} has Email-Id {self.email}"