# Generated by Django 5.0 on 2024-02-13 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrperformance', '0006_alter_attendancerecord_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='type',
            field=models.ForeignKey(blank=True, default=1, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='hrperformance.timelogtype'),
        ),
    ]
