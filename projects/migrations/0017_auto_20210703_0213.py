# Generated by Django 3.1.2 on 2021-07-03 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_project_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='filter',
            field=models.TextField(default='filter-app', max_length=30),
        ),
    ]
