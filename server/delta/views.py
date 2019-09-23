import django
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import json
from django.http import JsonResponse
from delta.models import status,led
from .forms import nodemcu
from django.db import connection
from django.views.decorators.csrf import csrf_protect
def node(request):
    response={'moisture':678
    }
    return JsonResponse(response)
    #queryset = led.objects.all()
def show(request):
    ##form=nodemcu(request.POST or None)
    obj=get_object_or_404(status, id=5)
    ##if form.is_valid():
    ##    form.save()
    #obj= status.objects.get(id=5)
    ##x=len(request.POST)
    mydata=json.loads(request.body.decode('utf-8'))
    ##obj.moisture=json.loads(receiveddata)
    obj.moisture=mydata["moisture"]
    obj.save()
    obj2=get_object_or_404(led,id=1)
    ##m=json.loads(f)
    #id_ = self.kwargs.get("id")
    if request.method =='POST':
        response={
        'method':request.method,
        'moisture':obj.moisture,
        'state':obj2.order
        }
        return JsonResponse(response)
    elif request.method =='GET':
        response={
        'method':request.method,
        'moisture':m["moisture"],
        'state':obj2.order
        }
        return JsonResponse(response)

##    response={
##    'abas':f,
##    'state':'on',
##    }
    ##return JsonResponse(response)
    ##if request.headers['connection'] =='close':
        ##connection.close()
def function(request):
    obj= status.objects.get(id=5)
    content={
    'title': obj.title ,
    'state': obj.moisture
    }
    return render(request,'show.html',content)

def off(request):
    obj= led.objects.get(id=1)
    obj.order='off'
    obj.position='off'
    #obj.slug='on to off'
    obj.save( )
#    post=led.objects.create(order='off',position='off')
#    post.save()
    content={
    'order': obj.order ,
    'position': obj.position
    }
    return render(request,'base.html',content)
def on(request):
    obj= led.objects.get(id=1)
    obj.order='on'
    obj.position='on'
    #obj.slug='off to on'
    obj.save()
    content={
    'order': obj.order ,
    'position': obj.position
    }
    return render(request,'base.html',content)
def homepage(request):
#    person= {'firstname': 'farzin', 'lastname': 'Daniels'}
#    weather= "sunny"
#    context= {
#        'person': person,
#        'weather': weather,
#        }
    return render(request,'base.html')
