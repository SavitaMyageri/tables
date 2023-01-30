from django.shortcuts import render
from app.models import *

def display_topic(request):
    QST=Topic.objects.all()
    d={'Topic':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=WebPage.objects.all()
    
    
    d={'WebPage':QSW}
    return render(request,'display_webpage.html',d)

def display_AccessRecord(request):
    QSA=AccessRecords.objects.all()
    d={'AccessRecords':QSA}
    return render(request,'display_AccessRecord.html',d)
    
    
    