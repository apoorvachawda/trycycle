# Generated by Django 3.1.2 on 2020-10-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0011_auto_20201027_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]
