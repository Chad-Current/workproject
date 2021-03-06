# Generated by Django 3.0 on 2020-08-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('primary_key', models.BigIntegerField(primary_key=True, serialize=False)),
                ('badge_identifier', models.SmallIntegerField()),
                ('location', models.TextField()),
                ('talkgroup_assoc', models.CharField(max_length=255)),
                ('rssi', models.IntegerField()),
                ('mobile', models.BooleanField(default=False)),
                ('portable', models.BooleanField(default=False)),
                ('desc_issue', models.TextField()),
                ('issue_resolve', models.BooleanField(default=False)),
                ('desc_resolve', models.TextField()),
                ('time_stamp', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tickets',
                'managed': False,
            },
        ),
    ]
