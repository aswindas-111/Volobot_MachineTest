from rest_framework import generics
from .models import *
from .serializers import SectionSerializer, StudentSerializer

class SectionListCreateView(generics.ListCreateAPIView):
    '''API endpoint that allows the listing and creation of sections'''
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''API endpoint that allows the retrieval, updating, and deletion of a specific section'''
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    '''API endpoint that allows the listing and creation of students'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''API endpoint that allows the retrieval, updating, and deletion of a specific student'''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
