# Generated by Django 3.2 on 2021-05-12 23:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('coupon_code', models.CharField(max_length=40)),
                ('expiry_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
