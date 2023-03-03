from django.contrib import admin
from .models import Profile

class ProfileAdmin (admin.ModelAdmin):
    list_display = ('id','email','program','created_at')
    list_display_links = ('id','email')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Profile,ProfileAdmin)