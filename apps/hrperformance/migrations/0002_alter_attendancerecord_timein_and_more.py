# Generated by Django 5.0 on 2024-02-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrperformance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='timein',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='timeout',
            field=models.DateTimeField(),
        ),
    ]
