# Generated by Django 3.1.2 on 2021-08-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_project_bottom_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
