from django.shortcuts import render
import rest_framework

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'uses HTTP methods as functions get, post, put, patch, delete',
            'Is similar to traditional django view',
            'Gives you most control over you aplication logic',
            'Is mapped manually to urls'
        ]
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
        