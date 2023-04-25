from django.db import models
from util.models import DefaultTable
from django.contrib.auth.hashers import make_password
from util.models import LoginType
from util.models import Status
from util.models import Gender

# Create your models here.

class Employee(models.Model):
    employeeName = models.TextField()
    
class User(DefaultTable):
    # mostly email id
    user_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, null=False)
    dob = models.DateField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)

class Login(DefaultTable):
    # change the password on login change
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,null=False,blank=False)
    password = models.CharField(max_length=30, null=False)
    login_type = models.ForeignKey(LoginType, on_delete=models.CASCADE,null=False,blank=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)
    comments = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.s_password = make_password(self.s_password)
        super(Login, self).save(*args, **kwargs)

