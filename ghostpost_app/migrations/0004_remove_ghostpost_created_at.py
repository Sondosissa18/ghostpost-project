# Generated by Django 3.1.3 on 2020-11-18 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost_app', '0003_auto_20201118_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='created_at',
        ),
    ]
