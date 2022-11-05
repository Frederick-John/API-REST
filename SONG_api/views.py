from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import SongSerializer

# Create your views here.

class SONGListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the SONG items for given requested user
        '''
        Song = Song.objects.filter(user = request.user.id)
        serializer = SongSerializer(Song, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the SONG with given SONG data
        '''
        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'), 
            'age': request.data.get('age')
        }
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)