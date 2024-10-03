from django.db import models
import uuid
import datetime

# Create your models here.
class Expense(models.Model):
    expenseId = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 200, blank = False, null = False)
    description = models.TextField(max_length = 500, blank = False, null = False)
    category = models.CharField(max_length = 50, blank = False, null = False)
    amount = models.FloatField(null = False, blank = False)
    expenseDate = models.DateTimeField(null = False, default = datetime.datetime.now)
    creationDate = models.DateTimeField(null = False, default = datetime.datetime.now)
    currency = models.CharField(max_length = 50, null = False, blank = False, default = 'INR')
    status = models.CharField(max_length = 50, null = False, blank = False, default = 'PENDING')
    
    def __str__(self):
        return f"{self.title} {self.expenseId}"