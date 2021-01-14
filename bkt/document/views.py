from django.shortcuts import render,redirect

from .models import *
from .filters import OrderFilter
# Create your views here.
def home(request):
    radars = Radar.objects.filter(display=True)

    context = {'radars':radars}

    return render(request,'document/index.html', context)


def radarDetail(request,slug):
    
    radar = Radar.objects.get(slug=slug)
    contents = Content.objects.filter(radar=radar)
    contentAs = ContentA.objects.filter(radar=radar)
    contentBs = ContentB.objects.filter(radar=radar)

    myFilter = OrderFilter(request.GET, queryset=contentBs)
    contentBqs = myFilter.qs

    context = {'radar':radar, 'contents':contents,'contentBqs':contentBqs, 'myFilter': myFilter}
    return render(request,'document/detail.html', context)


def searchContent(request):
    radars = Radar.objects.all()
    contentBs = ContentB.objects.all()
    myFilter = OrderFilter(request.GET, queryset=contentBs)

    contentBs = myFilter.qs
    context = {'contentBs':contentBs, 'myFilter': myFilter}
    
    return render(request,'document/search.html', context)