# Generated by Django 2.2.24 on 2024-01-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20240109_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]