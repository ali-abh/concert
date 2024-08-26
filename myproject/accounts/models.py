from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    family = models.CharField(null=True,max_length=20)
    age = models.IntegerField(default=19)
    nationalCode = models.IntegerField()
    phoneNumber = models.IntegerField()
    man = 1
    woman = 2
    status_choices = (("man","مرد"),("woman","زن"))
    