# Generated by Django 3.1.2 on 2021-07-05 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0007_auto_20210705_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 5, 19, 2, 16, 477697)),
        ),
    ]
