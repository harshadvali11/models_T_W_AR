from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length


def insert_topic(request):
    tn=input('enter topic')

    TTO=Topic.objects.get_or_create(topic_name=tn)
    bl=TTO[1]
    if bl:
        TO=TTO[0]
        TO.save()
        #return HttpResponse('Topic is created')
        d={'topics':Topic.objects.all()}

        return render(request,'retrieve_topics.html',d)
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
        #return HttpResponse('webpage is created')
        d={'webpages':Webpage.objects.all()}
        return render(request,'retrieve_webpages.html',d)

    else:
        return HttpResponse('Topic is not there so i cant create ur webepage object')


def retrieve_topics(request):

    d={'topics':Topic.objects.all()}
    return render(request,'retrieve_topics.html',d)



def retrieve_webpages(request):
    QLWO=Webpage.objects.filter(topic_name='Cricket')
    QLWO=Webpage.objects.exclude(topic_name='Cricket')
    QLWO=Webpage.objects.all()[::-2]
    QLWO=Webpage.objects.all().order_by('name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.all().order_by('-name')

    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    
    

    d={'webpages':QLWO}
    return render(request,'retrieve_webpages.html',d)









