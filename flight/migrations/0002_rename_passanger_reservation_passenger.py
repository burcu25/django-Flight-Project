# Generated by Django 4.1.1 on 2022-09-29 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='passanger',
            new_name='passenger',
        ),
    ]
