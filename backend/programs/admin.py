from django.contrib import admin
from .models import WellnessProgram

class WellnessProgramAdmin(admin.ModelAdmin):

    list_display = ('id','name','start_date','end_date','is_active','category')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(WellnessProgram,WellnessProgramAdmin)