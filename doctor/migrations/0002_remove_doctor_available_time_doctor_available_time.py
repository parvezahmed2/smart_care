# Generated by Django 4.2.8 on 2024-02-24 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='available_Time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='available_Time',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]