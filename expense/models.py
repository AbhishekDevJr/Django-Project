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
    
class Department(models.Model):
    department = models.CharField(max_length = 100, editable = True)
    
    def __str__(self):
        return f"{self.department}"
    
    class Meta:
        ordering = ['department']
        
class StudentID(models.Model):
    student_id = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.student_id}"
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name = "studentid", on_delete = models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField(unique = True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()
    
    def __str__(self):
        return f"{self.student_name}"
    
    class Meta:
        ordering = ['student_name']
        verbose_name = ['student']