# Generated by Django 4.0.6 on 2022-08-09 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=40)),
                ('actors', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
