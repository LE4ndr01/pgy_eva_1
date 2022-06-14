# Generated by Django 4.0.5 on 2022-06-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_producto_segundadescripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='segundadescripcion',
            new_name='seg_desc',
        ),
        migrations.AlterField(
            model_name='tipo',
            name='nombreTipo',
            field=models.CharField(max_length=50, verbose_name='Nombre Tipo'),
        ),
    ]
