'''
Serializers convert complez data types into
native python data types

These will then be easily rendered into json
which will be used with React on the client side
'''

from rest_framework import serializers
from .models import React  

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = [
            'user', 'team', 'organization'
        ]