from django.contrib.auth.models import AbstractUser
from django.db import models


# # Create your models here.
#
class User(AbstractUser):
    middle_name = models.CharField(max_length=25,blank=True,null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'CUSTOM_AUTH_USER_MODEL'
