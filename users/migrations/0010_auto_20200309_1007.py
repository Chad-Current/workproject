# Generated by Django 3.0 on 2020-03-09 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200306_0919'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='users_profile',
        ),
    ]
