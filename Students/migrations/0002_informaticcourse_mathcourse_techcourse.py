# Generated by Django 2.2.6 on 2022-09-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformaticCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('limit', models.IntegerField(default=120, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MathCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('limit', models.IntegerField(default=10, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TechCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=0, max_length=10, null=True)),
                ('limit', models.IntegerField(default=20, max_length=10)),
            ],
        ),
    ]
