# Generated by Django 3.0.3 on 2020-09-03 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200902_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 3, 7, 57, 1, 625888, tzinfo=utc)),
        ),
    ]