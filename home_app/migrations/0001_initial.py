# Generated by Django 4.1.7 on 2023-03-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_title', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=12)),
                ('district', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_icon', models.ImageField(upload_to='')),
                ('desktop_logo', models.ImageField(upload_to='')),
                ('mobile_logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MainText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField()),
            ],
        ),
    ]