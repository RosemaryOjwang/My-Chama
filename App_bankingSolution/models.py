from django.db import models
from random import random
import math
import datetime

# Create your models here.
#class UserLogin(models.Model):
class AccountOpening(models.Model):
    ACCOUNT_TYPES = (
        ('INDI', 'Individual'),
        ('PSHIP', 'Partnership'),
        ('CO', 'Company')

    )
    IDENTIFICATION_DOCUMENT = (
        ('ID', 'Kenyan Id'),
        ('AL', 'Kenyan Alien Id'),
        ('PPT', 'Passport')
    )
    NATIONALITY_CHOICES = (
        ('KE', 'KENYAN'),
        ('FG', 'FOREIGNER')
    )
    RESIDENCY_CHOICES = (
        ('RE', 'Resident'),
        ('NRE', 'Non-Resident')
    )
    DOB_CHOICES = (
        ('d_o_b', 'Date of Birth'),
        ('d_o_i', 'Date of Incorporation'),
        ('d_o_r', 'Date of Registration')
    )
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES)
    identification_doc = models.CharField(max_length=3, choices=IDENTIFICATION_DOCUMENT, default='ID')
    identity_number = models.CharField(max_length=10, unique=True, default=123456789)
    account_type = models.CharField(max_length=5, choices=ACCOUNT_TYPES)
    residency = models.CharField(max_length=3, choices=RESIDENCY_CHOICES)
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    company_business_name = models.CharField(max_length=155, blank=True)
    date_of_birth = models.CharField(max_length=5, choices=DOB_CHOICES)
    birth_date = models.DateField(default=datetime.date.today)
    account_number = models.IntegerField(default=00)
    
def __str__(self):
    account_number = math.floor(random(0.1,0.9))*1000
    return (self.first_name)

class Meta:
    db_table = 'AccountOpening'


#class TransactionMaintenance(models.Model)

