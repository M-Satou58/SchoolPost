# Generated by Django 4.0.5 on 2022-06-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenteconomy',
            name='name',
        ),
        migrations.AddField(
            model_name='studenteconomy',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studenteconomy',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]