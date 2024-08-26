from django.db import models
from accounts.models import Profile
# Create your models here.

class Concert(models.Model):
    class Meta:
        verbose_name="کنسرت"
    title = models.CharField(max_length=50)
    timeConcert = models.TimeField()
    location = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)


class TimeConert(models.Model):
    concert = models.ForeignKey(Concert,on_delete=models.PROTECT)
    location = models.ForeignKey(Location,on_delete=models.PROTECT)
    startTime = models.TimeField()
    numberOfSeats = models.IntegerField(null=True)
    def __str__(self):
        return "time: {} title: {} location: {}".format(self.startTime,Concert.title,Location.address)




class TicketModel(models.Model):
    profileModel = models.ForeignKey(Profile,on_delete=models.PROTECT,max_length=20)
    timeModel = models.ForeignKey("TimeConert",on_delete=models.PROTECT,max_length=20)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    def __str__(self):
        return "profile: {} concert time: {}".format(Profile.name,TimeConert.startTime)