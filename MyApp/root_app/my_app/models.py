from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserRegisterInfo(models.Model):
    #refernce the value from USERS
    #to user
    #USER default consist of username, password
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    #return toSTring to dipplsay data
    def __str__(self):
        return self.user.username

    
