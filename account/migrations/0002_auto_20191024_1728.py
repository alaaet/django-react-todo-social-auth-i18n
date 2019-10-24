# Generated by Django 2.2.6 on 2019-10-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='family_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='given_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='image_url',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_social_account',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='provider',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='social_token',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
