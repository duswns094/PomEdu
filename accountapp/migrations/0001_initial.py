# Generated by Django 4.0 on 2022-01-02 10:19
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
def forwards_func(apps, schema_editor):
    # 현재 모든 유저에 대해 Profile을 만들어주자.
    # settings.AUTH_USER_MODEL = 'auth.User'
    auth_user_model = settings.AUTH_USER_MODEL.split('.')
    # *는 언팩킹함
    User = apps.get_model(*auth_user_model)
    Profile = apps.get_model('accountapp', 'Profile')

    for user in User.objects.all():
        print('create profile for user#{}'.format(user.pk))
        Profile.objects.create(user=user)

def backwards_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('birth_date', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(forwards_func, backwards_func),
    ]
