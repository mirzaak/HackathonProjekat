from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



class Lightning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    switch = models.BooleanField(default=False)




