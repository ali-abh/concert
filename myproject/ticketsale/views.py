from django.shortcuts import render
from ticketsale.models import Concert
from ticketsale.models import Location,TimeConert

#from django.http import HttpResponse
# Create your views here.
def concertListView(request):
    concerts = Concert.objects.all()
    context={
        "concertlist":concerts
    }
    return render(request,"ticketsale/concertlist.html",context)


def locationListView(request):
    locations = Location.objects.all()
    context={
        "locationtlist":locations
    }
    return render(request,"ticketsale/locationlist.html",context)


def TimeListView(request):
    timeconcert = TimeConert.objects.all()
    context = {
        "TimeList": timeconcert
    }
    return render(request,"ticketsale/TimeList.html",context)