# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


class HelloApiView(APIView):
    """Test API Views"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,format =None):
        """Return a listof API View features"""

        an_apiview= [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
            ]

        return Response({'message':"Hello","an_api":an_apiview})

    def post(self ,request):
        """Creates a hello message wit your name"""
        serializer = serializers.HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response ({'message':message})

        else:
            return Response(
            serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk = None):
        """Handle updating an object"""
        return Response ({'method':'put'})

    def patch(self,request,pk = None):
        """Patch request only update field provided in the request"""
        return Response ({'method':'patch'})

    def delete(self,request,pk = None):
        """Delete an object"""
        return Response ({'method':'delete'})
