# Generated by Django 3.1.3 on 2020-11-26 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0005_auto_20201107_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='image_height',
            field=models.PositiveIntegerField(default=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bio',
            name='image_width',
            field=models.PositiveIntegerField(default=300),
            preserve_default=False,
        ),
    ]
