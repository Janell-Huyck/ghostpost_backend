# Generated by Django 3.0.7 on 2020-06-23 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghostpost',
            name='title',
        ),
    ]
