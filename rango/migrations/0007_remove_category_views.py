# Generated by Django 2.1.5 on 2023-02-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_auto_20230209_0232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]