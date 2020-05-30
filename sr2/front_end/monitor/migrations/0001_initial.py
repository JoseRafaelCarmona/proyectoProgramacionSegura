# Generated by Django 3.0.5 on 2020-05-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administradores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAdmin', models.CharField(max_length=30)),
                ('nombreUsuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=50)),
                ('ip_servidor', models.CharField(max_length=16)),
                ('tokenTelegram', models.CharField(max_length=50)),
                ('telegram', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='servidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(max_length=18)),
                ('ip', models.CharField(max_length=18)),
                ('hostname', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=70)),
            ],
        ),
    ]
