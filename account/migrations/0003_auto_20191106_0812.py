# Generated by Django 2.2.6 on 2019-11-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191106_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='date_to',
            field=models.DateField(),
        ),
    ]
