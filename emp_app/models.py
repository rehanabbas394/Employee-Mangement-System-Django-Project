from django.db import models
from django.contrib.auth.models import User

class LeaveApplication(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    status_choices = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField(default=False)
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    

class user(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    def __str__(self):
        return self.name

class employee(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=10)
    dep = models.CharField(max_length=50,null=True)
    role = models.CharField(max_length=50,null=True)
    salary = models.IntegerField(null=True)
    address = models.TextField(null=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
   
    
    
class Admin_user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    address = models.TextField()
    # user = models.ForeignKey(user, on_delete=models.CASCADE)
    