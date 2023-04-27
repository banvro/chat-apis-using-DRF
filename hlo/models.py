from django.db import models

# Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, null=True, blank=True)
#     location = models.PointField(null=True, blank=True)                              #30.71162683965989, 76.71142322625579
#     lat = models.CharField(max_length=500)
#     lon = models.CharField(max_length=500) 
#     NearUser = models.ManyToManyField('WhosThatAPIs.UserProfile', null=True, blank= True)

#     def __str__(self):
#         return str(self.user)