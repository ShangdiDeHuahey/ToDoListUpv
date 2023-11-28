from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import *
from .models import *


class IndexView(TemplateView):
    template_name = 'index.html'

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    
class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

class UpdateCompletion(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

    def perform_update(self, serializer):
        serializer.save(Completed=True)

class UpdateCompletion(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

    def perform_update(self, serializer):
        serializer.save(Completed=True)

