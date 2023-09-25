from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView  # BUG, not using it at/ using generics...
from rest_framework.response import Response
from .models import User, Team, Organization, Post
from .serializer import UserLoginSerializer, TeamLoginSerializer, OrganizationLoginSerializer, PostSerializer

# Create your views here.
# class ReactView(generics.ListCreateAPIView):
# class ReactView(APIView):
#     serializer_class = ReactSerializer

#     def get(self, request):
#         output = [
#             {
#              'user':output.user,
#              'team':output.team,
#              'organization':output.organization
#              }
#              for output in React.objects.all()
#                    ]
#         return Response(output)

#     def post(self, request):
#         serializer = self.serializer_class(data= request.data)
#         if serializer.is_valid(raise_exception= True):
#             # We save the data
#             serializer.save()
#             return Response(serializer.data)


### Login VIEWS ###

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def get(self, request):
        output = [
            {
                'user_name':output.user_name,
                'email':output.email,
                'team':output.team,
                'organization':output.organization
            }
            for output in User.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)


class TeamLoginView(APIView):
    serializer_class = TeamLoginSerializer

    def get(self, request):
        output = [
            {
                'team_name':output.team_name,
                'admin_email':output.admin_email
            }
            for output in Team.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)


class OrganizationLoginView(APIView):
    serializer_class = OrganizationLoginSerializer
    
    def get(self, request):
        output = [
            {
                'organization_name':output.organization_name,
                'admin_email':output.admin_email
            }
            for output in Organization.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)


### POSTS VIEWS ###

class PostView(APIView):
    serializer_class = PostSerializer

    def get(self, request):
        output = [
            {
                'name':output.name,
                'description':output.description,
                'content':output.content
            }
            for output in Post.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)





