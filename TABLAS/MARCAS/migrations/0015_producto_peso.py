# Generated by Django 5.1 on 2024-08-23 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MARCAS', '0014_rename_animal_animal_nombre_producto_consis'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
