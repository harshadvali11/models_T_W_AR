from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topic')

    TTO=Topic.objects.get_or_create(topic_name=tn)
    bl=TTO[1]
    if bl:
        TO=TTO[0]
        TO.save()
        return HttpResponse('Topic is created')
    else:
        return HttpResponse('Topic is already present')

'''
#getting PO by using get method so if object is not there then Throws an error
def insert_webpage(request):
    tn=input('enter topicname')

    TO=Topic.objects.get(topic_name=tn)
    na=input('enter name')
    url=input('enter url')
    email=input('enter email')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
    WO.save()
    return HttpResponse('webpage is created')
'''

def insert_webpage(request):
    tn=input('enter topicname')
    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        na=input('enter name')
        url=input('enter url')
        email=input('enter email')

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
        WO.save()
        return HttpResponse('webpage is created')
    else:
        return HttpResponse('Topic is not there so i cant create ur webepage object')
















