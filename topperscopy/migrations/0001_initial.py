# Generated by Django 5.1.1 on 2024-09-05 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='topper_copy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Paper', models.CharField(max_length=50)),
                ('Rank', models.PositiveIntegerField()),
                ('Optional', models.CharField(max_length=25)),
                ('Photo', models.ImageField(null=True, upload_to='toppers/photo')),
                ('File', models.FileField(upload_to='toppers/copy')),
                ('Likes', models.PositiveIntegerField()),
                ('Added_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='topper_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Paper', models.CharField(max_length=50)),
                ('Rank', models.PositiveIntegerField()),
                ('Photo', models.ImageField(null=True, upload_to='toppers/photo')),
                ('Link', models.URLField(null=True)),
                ('Added_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
