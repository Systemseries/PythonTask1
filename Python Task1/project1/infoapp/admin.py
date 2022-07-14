from django.contrib import admin
from .models import clientinfo,user2

# Register your models here.
@admin.register(clientinfo)
class clientadmin(admin.ModelAdmin):
    list_display=['client_id','client_name','created_at','created_by']

@admin.register(user2)
class clientadmin1(admin.ModelAdmin):
    list_display=['user_id','user_name','project_name','created_at','created_by','updated_at']

