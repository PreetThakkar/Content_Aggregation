# Generated by Django 3.1.7 on 2021-04-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BBC_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Byteiota_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Engadget_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Medium_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
            ],
        ),
    ]
