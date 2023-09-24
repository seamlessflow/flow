from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView  # BUG, not using it at/ using generics...
from rest_framework.response import Response
from .models import React
from .serializer import ReactSerializer

# Create your views here.
# class ReactView(generics.ListCreateAPIView):
class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        output = [
            {
             'user':output.user,
             'team':output.team,
             'organization':output.organization
             }
             for output in React.objects.all()
                   ]
        return Response(output)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception= True):
            # We save the data
            serializer.save()
            return Response(serializer.data)

