# Generated by Django 4.0 on 2022-01-13 10:41

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacherapp', '0002_alter_teacher_subject'),
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateField(auto_now_add=True)),
                ('is_activated', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='lecture/')),
                ('subject', models.CharField(choices=[('Korean', '국어'), ('Math', '수학'), ('English', '영어'), ('Science', '과학'), ('Social', '사회')], max_length=20)),
                ('description', models.TextField(null=True)),
                ('is_activated', models.BooleanField(default=True)),
                ('opendate', models.DateField(null=True)),
                ('cost', models.IntegerField()),
                ('students', models.ManyToManyField(related_name='lectures', through='lectureapp.Enrollment', to='studentapp.Student')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lecture', to='teacherapp.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='lectureapp.lecture')),
            ],
        ),
        migrations.AddField(
            model_name='enrollment',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lectureapp.lecture'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentapp.student'),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('student', 'lecture')},
        ),
    ]
