from django.shortcuts import render
from .serializers import *
from .models import Todo
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions

# Create your views here.

class SignUp(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=SignUpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'User Created'})
        return Response(data=ser.errors)

class TodoView(ModelViewSet):
    serializer_class=TodoSer
    queryset=Todo.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def create(self,request):
        ser=TodoSer(data=request.data)
        if ser.is_valid():
            ser.save(user=request.user)
            return Response({'msg':'Todo Created'})
        return Response(data=ser.errors)
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
