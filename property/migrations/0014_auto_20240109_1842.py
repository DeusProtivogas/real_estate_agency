# Generated by Django 2.2.24 on 2024-01-09 15:04

import phonenumbers
from django.db import migrations, transaction

def change_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        phone_number = phonenumbers.parse(
                flat.owners_phonenumber,
                "RU"
            )
        flat.owner_pure_phone = None
        if phonenumbers.is_valid_number(phone_number):
            flat.owner_pure_phone = phonenumbers.format_number(
                phone_number,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            )
        flat.save()



def change_phone_back(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20240109_1841'),
    ]

    operations = [
        migrations.RunPython(change_phone, change_phone_back),
    ]
