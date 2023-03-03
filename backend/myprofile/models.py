import email
from django.db import models
from django.contrib.auth import get_user_model
from programs.models import WellnessProgram
from django.conf import settings
from datetime import datetime


User = get_user_model()

class Profile(models.Model):
    email = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=60)
    program = models.ForeignKey(WellnessProgram, on_delete=models.CASCADE,blank=True)
    weight = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    height = models.IntegerField(blank=True)
    muscle_mass = models.DecimalField(max_digits=4,decimal_places=2,blank=True)
    body_fat_mass = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    visceral_fat = models.DecimalField(max_digits=4,decimal_places=2,blank=True)
    meal_plan = models.FileField(upload_to=f'documents/str({User})/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.email )+ ' ' + str(self.program)


