# Generated by Django 2.1.2 on 2018-11-08 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nephrosis', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Patient',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='test_text',
            new_name='patient_text',
        ),
    ]
