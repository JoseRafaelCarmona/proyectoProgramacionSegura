# Generated by Django 3.0.7 on 2020-07-09 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_auto_20200709_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='relacion_user_servidor',
            name='estatus',
            field=models.BooleanField(default=0),
        ),
    ]
