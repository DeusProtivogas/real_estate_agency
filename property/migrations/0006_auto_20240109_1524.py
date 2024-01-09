
from django.db import migrations


def set_new_building_status(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        flat.new_building = True if flat.construction_year >= 2015 else False
        flat.save()

def move_backward(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    for flat in flats.objects.all():
        flat.new_building = None
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0005_auto_20240109_1523'),
    ]

    operations = [
        migrations.RunPython(set_new_building_status, move_backward)
    ]
