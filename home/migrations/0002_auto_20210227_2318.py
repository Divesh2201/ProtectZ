# Generated by Django 3.1.6 on 2021-02-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='disease',
            new_name='some_var',
        ),
    ]