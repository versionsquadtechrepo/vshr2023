from django.db import models

# Create your models here.

class DefaultTable(models.Model):
    creationname = models.CharField(max_length=64)
    creationdate = models.DateTimeField(auto_now_add=True)
    revisionname = models.CharField(max_length=64)
    revisiondate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Status(DefaultTable):
    status = models.CharField(max_length=20,null=False,blank=False)

    
class EmailType(DefaultTable):
    email_type = models.CharField(max_length=20,null=False,blank=False)

class LoginType(DefaultTable):
    login_type = models.CharField(max_length=20,null=False,blank=False)

class PhoneType(DefaultTable):
    phone_type = models.CharField(max_length=20,null=False,blank=False)

class LocationType(DefaultTable):
    location_type = models.CharField(max_length=20,null=False, blank=False)

class LocationAssocType(DefaultTable):
    location_assoc_type = models.CharField(max_length=20,null=False, blank=False)

class Location(DefaultTable):
    location_name = models.CharField(max_length=200,null=False, blank=False)
    location_type = models.ForeignKey(LocationType,on_delete=models.CASCADE,null=False, blank=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)

class LocationAssoc(DefaultTable):
    location_from = models.ForeignKey(Location,on_delete=models.CASCADE,null=False, blank=False,related_name='location_from')
    location_to = models.ForeignKey(Location,on_delete=models.CASCADE,null=False, blank=False,related_name='location_to')
    location_assoc_type = models.ForeignKey(LocationAssocType,on_delete=models.CASCADE,null=False, blank=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)

class PhoneCountryCode(DefaultTable):
    country_code = models.CharField(max_length=10,null=False,blank=False)
    country = models.ForeignKey(Location,on_delete=models.CASCADE, null=False,blank=False)

class Gender(DefaultTable):
    gender = models.CharField(max_length=20,null=False,blank=False)

class EmployeeRoleType(DefaultTable):
    employee_role_type = models.CharField(max_length=20,null=False,blank=False)

