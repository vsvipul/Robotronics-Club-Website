# Generated by Django 2.0 on 2018-01-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotronics', '0004_project_tutorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('Coord16', 'Coord16'), ('Coord', 'Coord'), ('Team', 'Team'), ('Team16', 'Team16')], default='Team', max_length=20),
        ),
    ]
