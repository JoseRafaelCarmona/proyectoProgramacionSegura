# Generated by Django 3.0.7 on 2020-07-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servidor',
            name='numero_procesadores',
            field=models.CharField(default='0', max_length=1),
        ),
    ]
