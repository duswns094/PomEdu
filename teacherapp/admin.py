from django.contrib import admin

# Register your models here.
from teacherapp.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'subject']
    list_display_links = ['name']

admin.site.register(Teacher, TeacherAdmin)