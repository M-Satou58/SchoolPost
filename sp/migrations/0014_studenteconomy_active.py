# Generated by Django 4.0.5 on 2022-06-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0013_alter_studenteconomy_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenteconomy',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]