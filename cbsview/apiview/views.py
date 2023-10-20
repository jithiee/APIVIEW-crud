from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Student
from .serilizers import Studenterializers
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk 
        if id is not None:
            stu = Student.objects.get(pk = id)
            serializer = Studenterializers(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = Studenterializers(stu , many=True)
        return Response(serializer.data)
    
    def post(self,request,formate=None):
        serializer = Studenterializers(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'data created'  }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk = id)
        serializer = Studenterializers(stu, request.data)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'complete data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self,request,pk=None,format=None):
        id = pk 
        stu = Student.objects.get(pk = id)
        serializer = Studenterializers(stu, request.data,partial = True)
        if serializer.is_valid:
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id = pk
        stu = Student.objects.get(pk =id)
        stu.delete()
        return Response({'msg':'data Deleted'})
    
    
    
            
    
        
        
        
            