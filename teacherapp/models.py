from django.db import models
from django.urls import reverse

subject_choices = (
    ('Korean','국어'),
    ('Math','수학'),
    ('English','영어'),
    ('Science','과학'),
    ('Social','사회'),
)
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='teacher/', null=True)
    subject = models.CharField(max_length=20, choices=subject_choices, null=False)

    is_activated = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('teacherapp:detail', args=[self.id])