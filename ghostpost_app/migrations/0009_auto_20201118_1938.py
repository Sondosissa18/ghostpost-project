# Generated by Django 3.1.3 on 2020-11-18 19:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0008_auto_20201118_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
