# Generated by Django 3.1.2 on 2020-11-05 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0015_remove_cycle_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='billing',
        ),
    ]