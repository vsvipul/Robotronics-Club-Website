# Generated by Django 2.0 on 2018-03-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotronics', '0007_auto_20180228_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AddField(
            model_name='member',
            name='github',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='linkedin',
            field=models.CharField(max_length=500, null=True),
        ),
    ]