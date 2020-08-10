# Generated by Django 2.2.11 on 2020-08-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0160_patientconsultation_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientconsultation',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patientconsultation',
            name='verified_by',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
