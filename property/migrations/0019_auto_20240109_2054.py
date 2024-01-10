# Generated by Django 2.2.24 on 2024-01-09 15:55

from django.db import migrations, transaction


def fill_owner(apps, schema_editor):
    Owner = apps.get_model("property", "Owner")
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        with transaction.atomic():
            owner, created = Owner.objects.get_or_create(
                name=flat.owner,
                phone_number=flat.owners_phonenumber,
                phone_number_pure=flat.owner_pure_phone,
            )
            owner.save()

        with transaction.atomic():
            owner.flats.add(flat)
            owner.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20240109_2054'),
    ]

    operations = [
        migrations.RunPython(fill_owner),
    ]
