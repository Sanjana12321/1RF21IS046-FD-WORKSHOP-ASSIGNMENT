# Generated by Django 5.0.6 on 2024-06-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50)),
                ('college1', models.CharField(max_length=100)),
                ('course1', models.CharField(max_length=30)),
            ],
        ),
    ]
