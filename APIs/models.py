from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
import uuid
  
class User(AbstractUser):
    uid = models.UUIDField(primary_key = True, unique=True, default = uuid.uuid4, editable = False)
    username = models.CharField(max_length=250, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True,max_length=30)
    DateOfBirth = models.CharField(max_length=70)
    firebase_password = models.CharField(max_length=250, null=True, blank=True)
    firebase_uid = models.CharField(max_length=255, null=True, blank=True)
    profilepic = models.ImageField(upload_to='ProfilePic', null=True, blank=True)