from django.db import models
from util.models import Status
from util.models import Location
from django.utils.timezone import now
from util.models import DefaultTable
from util.models import PhoneCountryCode
from util.models import PhoneType
from util.models import EmailType


# Create your models here.
class Account(DefaultTable):
    # company Name
    account_name = models.CharField(max_length=200)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)

class AccountBranchType(DefaultTable):    
    account_branch_type = models.CharField(max_length=10)

class AccountBranch(DefaultTable):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=False,blank=False)
    branch_type = models.ForeignKey(AccountBranchType, on_delete=models.CASCADE,null=False,blank=False)
    branch_name = models.CharField(max_length=100)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)
    

class AccountBranchAddress(DefaultTable):
    #address 1 
    account = models.ForeignKey(AccountBranch, on_delete=models.CASCADE)
    domain = models.CharField(max_length=300)
    address1 = models.CharField(max_length=300,null=False, blank=False)
    address_line1 = models.CharField(max_length=300)
    address_line2 = models.CharField(max_length=300,blank=True)
    state = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='state')
    city = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='city')
    pin = models.CharField(max_length=20)
    country = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='country')  
    created_date = models.DateTimeField(default=now)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)
    


class AccountPhone(DefaultTable):
    account = models.ForeignKey(AccountBranch, on_delete=models.CASCADE)
    phone_type = models.ForeignKey(PhoneType,on_delete=models.CASCADE,null=False, blank=False)
    country_code = models.ForeignKey(PhoneCountryCode, on_delete=models.CASCADE,null=False,blank=False)   
    phone_numer = models.CharField(max_length=20,null=False,blank=False) 
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)

class AccountEmail(DefaultTable):
    account = models.ForeignKey(AccountBranch, on_delete=models.CASCADE)
    email_type = models.ForeignKey(EmailType,on_delete=models.CASCADE,null=False, blank=False)
    email = models.CharField(max_length=50,null=False,blank=False) 
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=False, blank=False)
    



