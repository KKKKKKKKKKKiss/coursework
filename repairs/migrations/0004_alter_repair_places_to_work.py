# Generated by Django 4.1.2 on 2022-10-23 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_alter_repair_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='places_to_work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='place_repairs', to='repairs.placestowork', verbose_name='Место для ремонта'),
        ),
    ]