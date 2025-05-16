from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer

@api_view(['GET', 'POST'])
def create_reminder(request):
    if request.method == 'GET':
        return Response({"message": "Send a POST request with reminder data to create a reminder."})
    
    elif request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
