# Generated by Django 3.1.2 on 2021-07-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20210706_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bottom_row',
            field=models.TextField(blank=True, null=True),
        ),
    ]
