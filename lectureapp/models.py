from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField

from studentapp.models import Student
from teacherapp.models import Teacher

subject_choices = (
    ('Korean','국어'),
    ('Math','수학'),
    ('English','영어'),
    ('Science','과학'),
    ('Social','사회'),
)
# Create your models here.
class Lecture(models.Model):
    name = models.CharField(max_length=100, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='lecture', null=True)
    image = models.ImageField(upload_to='lecture/', null=True, blank=True)
    subject = models.CharField(max_length=20, choices=subject_choices, null=False)
    description = models.TextField(null=True,blank=True)
    is_activated = models.BooleanField(default=True)
    students = models.ManyToManyField(Student, through='Enrollment',related_name='lectures')
    opendate = models.DateField(null=True)
    cost = models.IntegerField(null=False)

    def __str__(self):
        return f'{self.name}'

class Video(models.Model):
    name = models.CharField(max_length=100, null=False)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='video', null=False)
    video = EmbedVideoField()
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True,null=False)
    updated_at = models.DateField(auto_now=True,null=False)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    joined_at = models.DateField(auto_now_add=True,null=False)
    is_activated = models.BooleanField(default=True)
    class Meta:
        unique_together = ('student', 'lecture')
