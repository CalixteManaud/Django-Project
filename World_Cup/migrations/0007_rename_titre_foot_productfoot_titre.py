# Generated by Django 4.1.3 on 2023-02-08 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('World_Cup', '0006_categoryfoot_commandefoot_productfoot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productfoot',
            old_name='titre_foot',
            new_name='titre',
        ),
    ]