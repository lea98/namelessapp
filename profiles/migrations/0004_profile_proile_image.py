# Generated by Django 2.2 on 2020-09-04 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='proile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
