from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

teaBrew = [
    {
        'teaBrand':'Kim Guan Guan',
        'teaAmount':'1 tablespoon',
        'steepTime':'2mins 15sec',
        'condenseMilk':'1.5 tablespoon',
        'evaporatedMilk':'1.5 tablespoon',
        'verdict':'Very Awesome!'
    },
    {
        'teaBrand':'Kim Guan Guan',
        'teaAmount':'1 tablespoon',
        'steepTime':'2mins 15sec',
        'condenseMilk':'1 tablespoon',
        'evaporatedMilk':'1 tablespoon',
        'verdict':'before this one is better. can try 1.25 spoon!'
    }
]

def home(request):
    context={
        'teaBrew' : teaBrew
    }
    return render(request,'teatime/home.html',context)