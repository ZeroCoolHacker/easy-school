# Generated by Django 4.2.1 on 2023-05-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_guardian_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionform',
            name='date_signed',
            field=models.DateField(auto_now_add=True),
        ),
    ]
