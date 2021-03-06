# Generated by Django 3.1.2 on 2021-07-05 19:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20210705_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('geopandas', 'GeoPandas'), ('pandana', 'Pandana'), ('sklearn', 'Scikit-Learn'), ('dash', 'Plotly Dash'), ('osmnx', 'OSMnx'), ('qgis', 'QGIS'), ('python', 'Python'), ('sql', 'SQL'), ('grasshopper', 'Grasshopper')], default=('python', 'Python'), max_length=64),
        ),
    ]
