from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from .serializers import taskSerializer
from .models import taskModel

# Create your views here.
class taskApiView(APIView):
    def get(self,request):
        task_obj = taskModel.objects.all()

        #serializing model object
        serializer = taskSerializer(task_obj,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        #serializing data

        serializer =taskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class taskApiIDView(APIView):
    def get_object(self,id):
        try:
          task_object = taskModel.objects.get(id=id)
          return task_object
        except taskModel.DoesNotExist:
            return None
    

    def get(self,request,id):
        instance =self.get_object(id)

        if instance is None:
            return Response({'error':'data not found'})
        #serializing data
        serializer= taskSerializer(instance=instance)
        return Response(serializer.data)
    
    def put(self,request,id):
        instance = self.get_object(id)
        if instance is None:
            return Response({'error':'data not found'})
        serializer = taskSerializer(instance=instance,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,id):
        instance = self.get_object(id)
        if instance is None:
            return Response({'error':'data not found'})
        instance.delete()
        return Response({'msg':'data deleted successfully'})
