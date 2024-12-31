from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User

import datetime

class MissingRibApiView(APIView):
    def get(self, *args, **kwargs):
        '''
        List all users in database
        '''
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create new user account with info
        '''
        data = {
            'username': request.data.get('username'),
            'password': request.data.get('password'),
            'name': request.data.get('name'),
            'age': request.data.get('age')
        }
        serializer = UserSerializer(data=data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def index(request):
        now = datetime.datetime.now()
        html = '<html lang="en"><body>It is now %s.</body></html>' % now
        return HttpResponse(html)