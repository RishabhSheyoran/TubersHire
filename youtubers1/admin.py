from django.contrib import admin

from .models import Youtuber
# Register your models here.

class Ytadmin(admin.ModelAdmin):
    list_display = ('id','name','subs_count','is_featured')
    search_fields = ('name','camera_type')
    list_filter =  ('city','camera_type')
    list_display_links = ('id','name')
    list_editable = ('is_featured',)


admin.site.register(Youtuber,Ytadmin)
