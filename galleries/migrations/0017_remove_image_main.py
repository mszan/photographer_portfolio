# Generated by Django 3.1.3 on 2020-11-08 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0016_image_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='main',
        ),
    ]
