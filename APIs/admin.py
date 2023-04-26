from django.contrib import admin
from APIs.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    # ordering = ('email', 'first_name', 'last_name', 'is_staff', 'last_login', 'profilepic' )
    list_display = ('uid', 'email', 'phone_number', 'first_name', 'is_active', 'date_joined') # Added last_login
    
    fieldsets = (
        (None, {'fields': ('username', 'phone_number', 'email', 'uid', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'firebase_uid', 'firebase_password', 'DateOfBirth', 'profilepic')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),

       
    )