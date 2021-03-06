# Generated by Django 4.0 on 2022-01-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(null=True, upload_to='teacher/')),
                ('subject', models.CharField(max_length=20, null=True)),
                ('is_activated', models.BooleanField(default=True)),
            ],
        ),
    ]
