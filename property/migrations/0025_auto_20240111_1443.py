# Generated by Django 2.2.24 on 2024-01-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_auto_20240111_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры'),
        ),
    ]
