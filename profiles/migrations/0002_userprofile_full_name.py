# Generated by Django 4.2.8 on 2024-10-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default='Full Name', max_length=50),
        ),
    ]