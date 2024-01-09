# Generated by Django 2.2.24 on 2024-01-09 15:55

from django.db import migrations


def fill_owner(apps, schema_editor):
    Owner = apps.get_model("property", "Owner")
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phone_number=flat.owners_phonenumber,
            phone_number_pure=flat.owner_pure_phone,

        )

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_owner'),
    ]

    operations = [
        migrations.RunPython(fill_owner),
    ]
