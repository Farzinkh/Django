import django
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from delta.models import status,led
from django.db import connection
def show(request,f):
    obj= status.objects.get(id=5)
    obj.moisture=f
    obj.save()
    obj2=led.objects.get(id=1)
    if request.method =='POST':
        response={
        'method':request.method,
        'moisture':f,
        'state':obj2.order
        }
        return JsonResponse(response)
    elif request.method =='GET':
        response={
        'method':request.method,
        'moisture':f,
        'state':obj2.order
        }
        return JsonResponse(response)
    return HttpResponse("the name is {}".format(f))

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
