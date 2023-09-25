'''
Serializers convert complez data types into
native python data types

These will then be easily rendered into json
which will be used with React on the client side
'''

from rest_framework import serializers
from .models import User, Team, Organization, Post  

# class ReactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = React
#         fields = [
#             'user', 'team', 'organization', 'date_of_birth'
#         ]


### LOGIN SERIALIZERS ###

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_name', 'password', 'email', 'team', 'organization'
        ]

class TeamLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'team_name', 'password', 'admin_email'
        ]

class OrganizationLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'organization_name', 'password', 'admin_email'
        ]


### POSTS SERIALIZERS ###

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'name','description', 'content'
        ]