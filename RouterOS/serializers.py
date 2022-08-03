from rest_framework import serializers
from .models import *

class NasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NAS
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        
class ProfileGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileGroup
        fields = '__all__'
        
class PPPOESerializer(serializers.ModelSerializer):
    class Meta:
        model = PPPOE
        fields = '__all__'