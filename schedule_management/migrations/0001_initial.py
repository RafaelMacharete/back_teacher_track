# Generated by Django 5.1.6 on 2025-03-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_time', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=100)),
            ],
        ),
    ]
