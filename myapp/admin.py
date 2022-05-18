from django.contrib import admin
from .models import signup_master,notes

# Register your models here.
class signupAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','city','zipcode']

class notesAdmin(admin.ModelAdmin):
    list_display=["topic","selectop","des","myfile"]

admin.site.register(signup_master,signupAdmin)
admin.site.register(notes,notesAdmin)