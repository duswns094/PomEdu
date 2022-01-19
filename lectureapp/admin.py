from django.contrib import admin

# Register your models here.
from lectureapp.models import Lecture, Enrollment


class LectureAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'subject','teacher','is_activated','opendate']
    list_display_links = ['name']

admin.site.register(Lecture, LectureAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'lecture', 'student','joined_at','is_activated']
    list_display_links = ['lecture']

admin.site.register(Enrollment, EnrollmentAdmin)
