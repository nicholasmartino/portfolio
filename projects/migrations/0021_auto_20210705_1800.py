# Generated by Django 3.1.2 on 2021-07-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_delete_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='order',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]
