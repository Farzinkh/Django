import django
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from delta.models import status,led
from django.db import connection
def show(request,f):
    response={
    'abas':f,
    'state':'on',
    }
    return JsonResponse(response)
def function2(request,dade):
    if request.method=="POST":
        response={
        'view':request.method,
        'state':request.POST,
        }
        return JsonResponse(response)
    else:
        response={
        'state':"notdefine"
        }
        return JsonResponse(response)
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
    obj.save()
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
    obj.save()
    content={
    'order': obj.order ,
    'position': obj.position
    }
    return render(request,'base.html',content)
    #return HttpResponse("the name is {}".format(state))
def homepage(request):
#    person= {'firstname': 'farzin', 'lastname': 'Daniels'}
#    weather= "sunny"
#    context= {
#        'person': person,
#        'weather': weather,
#        }
    return render(request,'show.html')
