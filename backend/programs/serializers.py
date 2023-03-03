import imp
from rest_framework import serializers
from .models import WellnessProgram


class WellnessProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = WellnessProgram
        fields = '__all__'