from django.contrib import admin

# Register your models here.
from studentapp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'school','grade','phone_number']
    list_display_links = ['name']

admin.site.register(Student, StudentAdmin)