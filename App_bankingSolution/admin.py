from django.contrib import admin
from .models import AccountOpening, UserRegister

# Register your models here.
@admin.register(AccountOpening)
class AccountOpeningAdmi(admin.ModelAdmin):
    list_display = ['opening_date', 'first_name', 'second_name', 'last_name', 'account_number']
@admin.register(UserRegister)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
