from django.shortcuts import render
#from django.http import JsonResponse
#function api views??
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import GetAllTask

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    #return JsonResponse("Write something", safe=False)
    mydata={
        'var':'Example',
        'var1':'Overviews in rest framework Response'
    }
    return Response(mydata)


@api_view(['GET'])
def taskList(request):
    #get all data from database
    #sort by id
    tasks = Task.objects.all().order_by('-id')
    #send data to Serializer
    mydata = GetAllTask(tasks, many=True)
    return Response(data=mydata.data)

#One object detail
@api_view(['GET'])
def taskDetail(request,pk):
    #get one data Object from database
    task = Task.objects.get(id=pk)
    #send data to Serializer
    mydata = GetAllTask(task, many=False)
    return Response(data=mydata.data)

#Post data from client to database throught serializers
@api_view(['POST'])
def taskCreate(request):
    #get data from cliet form
    mydata = GetAllTask(data= request.data)
    #validate this data
    if mydata.is_valid():
        mydata.save()

    return Response(data=mydata.data)

#Update an id Object
@api_view(['POST'])
def taskUpdate(request,pk):
    #get data at id
    task = Task.objects.get(id=pk)
    #get data from cliet form
    mydata = GetAllTask(instance=task,data= request.data)
    #validate this data
    if mydata.is_valid():
        mydata.save()
        
    return Response(data=mydata.data)

#Delete an object
@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    #mydata = GetAllTask(instance=task,data=request.data)
    task.delete()
    return Response("Delete successfully")