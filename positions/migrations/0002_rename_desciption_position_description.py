# Generated by Django 4.0.4 on 2022-05-09 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='desciption',
            new_name='description',
        ),
    ]