from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

# create a class for the Todo model viewsets
class TodoView(viewsets.ModelViewSet):
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = TodoSerializer

    # define a variable and populate it
    # with the Todo list objects
    queryset = Todo.objects.all()
