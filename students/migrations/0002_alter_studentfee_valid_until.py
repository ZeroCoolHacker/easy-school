# Generated by Django 4.2.1 on 2023-05-13 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfee',
            name='valid_until',
            field=models.DateField(default=datetime.date(2023, 6, 1), verbose_name='Valid Until'),
        ),
    ]
