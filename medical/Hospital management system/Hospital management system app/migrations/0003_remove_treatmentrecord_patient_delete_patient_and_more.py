# Generated by Django 4.2.3 on 2023-08-02 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_patient_treatmentrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatmentrecord',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='TreatmentRecord',
        ),
    ]
