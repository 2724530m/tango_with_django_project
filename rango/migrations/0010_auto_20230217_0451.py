# Generated by Django 2.1.5 on 2023-02-17 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0009_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
