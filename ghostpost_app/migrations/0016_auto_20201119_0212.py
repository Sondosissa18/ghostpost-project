# Generated by Django 3.1.3 on 2020-11-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0015_auto_20201119_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='ghostpost',
            field=models.BooleanField(),
        ),
    ]
