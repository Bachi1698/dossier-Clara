# Generated by Django 2.2.12 on 2020-06-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/appartement')),
                ('lieu', models.CharField(max_length=255)),
                ('nombre_douche', models.IntegerField()),
                ('garage', models.BooleanField(default=False)),
                ('superficie', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'appartement',
                'verbose_name_plural': 'appartements',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/project')),
                ('types', models.CharField(choices=[('interior', 'interior'), ('exterior', 'exterior'), ('landing', 'landing')], max_length=255)),
                ('titre', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Poject',
                'verbose_name_plural': 'Pojects',
            },
        ),
    ]
