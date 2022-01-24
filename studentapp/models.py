from django.conf import settings
from django.db import models


class Student(models.Model):
    year_choices = (
        ('M1', '중1'), ('M2', '중2'), ('M3', '중3'),
        ('H1', '고1'), ('H2', '고2'), ('H3', '고3'),
        ('E4', '초4'), ('E5', '초5'), ('E6', '초6')
    )

    name = models.CharField(max_length=10)
    school = models.CharField(max_length=20, null=True)
    grade = models.CharField(max_length=2, choices=year_choices)
    phone_number = models.CharField(max_length=11)
    created_at = models.DateField(auto_now_add=True,null=False)

    def __str__(self):
        return f'{self.name}'

