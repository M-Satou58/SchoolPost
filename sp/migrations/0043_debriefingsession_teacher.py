# Generated by Django 4.0.5 on 2022-06-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sp', '0042_debriefingsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='debriefingsession',
            name='teacher',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
