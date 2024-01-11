
from django.db import migrations


def set_new_building_status(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building=None)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0005_auto_20240109_1523'),
    ]

    operations = [
        migrations.RunPython(set_new_building_status, move_backward)
    ]
