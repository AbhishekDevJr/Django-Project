from django.db import models
import datetime
import uuid

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200, null = False, blank = False)
    content = models.TextField(null = False, blank = False)
    createdAt = models.DateField(null = False, blank = False, default = datetime.date.today)
    blogId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    
    
    def __str__(self):
        return f"{self.title} {self.blogId}"