# Generated by Django 4.0.5 on 2022-06-13 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0015_alter_studenteconomy_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenteconomy',
            name='active',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=200, null=True),
        ),
    ]
