# Generated by Django 3.1.3 on 2020-11-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0015_auto_20201108_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]