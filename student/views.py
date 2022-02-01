from django.shortcuts import render,get_object_or_404
from.models import Student
from rest_framework import generics
from rest_framework.response import Response
from django.views. generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import StudentSerializer

# Create your views here.

# def student_list(request):
#     students = Student.objects.all()
#     return render(request,'students/list.html',{'students':students})


class StudentListView(ListView):
    model = Student
    template_name = "students/list.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "post_detail.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "students/new.html"
    fields = '__all__'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/update.html"
    fields = '__all__'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/delete.html"
    success_url = reverse_lazy('home')

 

 #Views for the Api
 
class StudentCreateApi(generics.CreateAPIView):
    queryset =  Student.objects.all()
    serializer_class =  StudentSerializer

class StudentApi(generics.ListAPIView):
    queryset =    Student.objects.all()
    serializer_class = StudentSerializer


class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset =  Student.objects.all()
    serializer_class =  StudentSerializer

class StudentDeleteApi(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class =  StudentSerializer
