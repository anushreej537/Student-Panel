from .serializers import RegistrationSerializer,CourseSerializer,StudentSerializer
from admin_panel.models import *
from rest_framework import generics
from rest_framework.response import Response


class RegistrationViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class RegistrationShowViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

class CourseViewSet(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseShowViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentShowViewSet(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentViewSet(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

class DeleteStudentViewSet(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'

class DestroyStudentViewSet(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
