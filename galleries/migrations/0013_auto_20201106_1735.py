# Generated by Django 3.1.3 on 2020-11-06 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0012_auto_20201106_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
