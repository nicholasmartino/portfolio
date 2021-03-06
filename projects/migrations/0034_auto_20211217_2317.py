# Generated by Django 3.1.2 on 2021-12-17 23:17

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0033_remove_project_bottom_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='filter',
            field=models.CharField(default='filter-gd', max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('qgis', 'QGIS'), ('python', 'Python'), ('js', 'JavaScript'), ('vue_js', 'Vue'), ('react_js', 'React'), ('mapbox', 'Mapbox-GL'), ('sql', 'SQL'), ('grasshopper', 'Grasshopper'), ('vray', 'V-Ray'), ('lumion', 'Lumion'), ('sketchup', 'SketchUp'), ('csharp', 'C#'), ('illustrator', 'Illustrator'), ('photoshop', 'Photoshop'), ('indesign', 'InDesign')], default=('python', 'Python'), max_length=112),
        ),
    ]
