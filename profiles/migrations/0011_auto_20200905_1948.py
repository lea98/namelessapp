# Generated by Django 2.2 on 2020-09-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20200905_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
