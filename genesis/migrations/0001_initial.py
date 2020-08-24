from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGenesisReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userGen', models.CharField(default='Username', max_length=255)),
                ('userOrg', models.CharField(default='Organization', max_length=255)),
                ('userFile', models.CharField(default='None', max_length=255)),
            ],
        ),
    ]
