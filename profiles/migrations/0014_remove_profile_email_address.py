# Generated by Django 2.2 on 2020-09-05 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_profile_email_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_address',
        ),
    ]
