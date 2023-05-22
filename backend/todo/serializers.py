from rest_framework import serializers #serializers from the REST framework
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # Create meta class
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')



