from django.contrib import admin
from todoapp.models import todo 



class todoAdmin(admin.ModelAdmin):
    list_display = ('tode_description','user','status','created_date','updated_date' )


# Register your models here.
admin.site.register(todo,todoAdmin)
