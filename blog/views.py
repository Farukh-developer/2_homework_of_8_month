from django.shortcuts import render
from rest_framework.generics import  RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView
from .models import ( Courses, Teachers, Students )
from .serializers import CoursesSerializer, TeachersSerializer, StudentsSerializer
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response


class CoursesCreateViewList(ListCreateAPIView):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    
class CoursesUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer
    permission_classes=[IsAuthenticated]
    
    
    
    
class TeachersCreateViewList(ListCreateAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    
class TeachersUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset=Teachers.objects.all()
    serializer_class=TeachersSerializer
    permission_classes=[permissions.DjangoModelPermissions]
    
    
    
    
    
    
    
class StudentsCreateViewList(ListCreateAPIView):
    queryset=Students.objects.all()
    serializer_class=StudentsSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    
class StudentsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset=Students.objects.all()
    serializer_class=StudentsSerializer
    permission_classes=[permissions.DjangoModelPermissions]
    
            