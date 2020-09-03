from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
"""
class UserModel(models.Model):
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
"""