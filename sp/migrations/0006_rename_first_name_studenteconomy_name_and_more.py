# Generated by Django 4.0.5 on 2022-06-11 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0005_studenteconomy_first_name_studenteconomy_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studenteconomy',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='studenteconomy',
            name='last_name',
        ),
    ]
