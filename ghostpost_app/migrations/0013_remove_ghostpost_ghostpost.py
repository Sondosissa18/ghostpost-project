# Generated by Django 3.1.3 on 2020-11-19 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0012_auto_20201119_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='ghostpost',
        ),
    ]