# Generated by Django 3.1.2 on 2021-07-05 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20210705_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='order',
        ),
    ]
