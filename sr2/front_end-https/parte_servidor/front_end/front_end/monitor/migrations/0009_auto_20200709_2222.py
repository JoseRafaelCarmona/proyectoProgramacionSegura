# Generated by Django 3.0.7 on 2020-07-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20200709_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacion_user_servidor',
            name='password_api',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
