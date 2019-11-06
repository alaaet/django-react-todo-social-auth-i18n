# Generated by Django 2.2.6 on 2019-11-06 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('st_line1', models.CharField(max_length=50)),
                ('st_line2', models.CharField(max_length=50)),
                ('postal_code', models.CharField(default='28013', max_length=5)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Address')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Business',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abbreviation', models.CharField(max_length=10)),
                ('call_code', models.CharField(max_length=50)),
                ('flag_url', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_from', models.DateField(auto_now_add=True)),
                ('date_to', models.DateField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('is_international', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Holiday',
            },
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_order', models.IntegerField(default=1)),
                ('period_order', models.IntegerField(default=1)),
                ('time_from', models.TimeField(auto_now_add=True)),
                ('time_to', models.TimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'WorkingHours',
            },
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.CharField(max_length=30)),
                ('date_from', models.DateField(auto_now_add=True)),
                ('date_to', models.DateField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vacation',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abbreviation', models.CharField(max_length=10)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Country')),
                ('holidays', models.ManyToManyField(to='account.Holiday')),
            ],
            options={
                'verbose_name': 'Region',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_business_admin', models.BooleanField(default=False)),
                ('rating_avg', models.IntegerField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Business')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='holidays',
            field=models.ManyToManyField(to='account.Holiday'),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Country')),
                ('holidays', models.ManyToManyField(to='account.Holiday')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Region')),
            ],
            options={
                'verbose_name': 'City',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Region'),
        ),
    ]
