# Generated by Django 3.1.2 on 2021-07-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0003_position_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
