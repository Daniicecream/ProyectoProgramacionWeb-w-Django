# Generated by Django 3.2.5 on 2021-07-05 16:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Lanzamientos', '0002_alter_lanzamiento_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='lanzamiento',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
