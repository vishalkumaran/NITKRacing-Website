# Generated by Django 3.0.4 on 2020-05-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0021_auto_20200520_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='subsystem_filter',
            field=models.IntegerField(choices=[(1, 'AERO'), (2, 'VD'), (3, 'PWR'), (4, 'ELEC')], default=0),
        ),
    ]
