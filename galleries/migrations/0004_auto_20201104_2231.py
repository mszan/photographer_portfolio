# Generated by Django 3.1.3 on 2020-11-04 22:31

from django.db import migrations, models
import galleries.models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_auto_20201104_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(upload_to=galleries.models.image_upload_path),
        ),
    ]
