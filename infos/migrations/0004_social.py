# Generated by Django 3.1.3 on 2020-11-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0003_auto_20201107_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('link', models.TextField()),
            ],
        ),
    ]
