# Generated by Django 3.0 on 2020-03-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200304_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='organiztion',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
