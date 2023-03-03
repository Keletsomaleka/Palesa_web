from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id','email','slug','program','weight','height','muscle_mass','body_fat_mass','visceral_fat')
