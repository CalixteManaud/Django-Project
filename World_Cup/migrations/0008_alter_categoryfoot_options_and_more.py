# Generated by Django 4.1.3 on 2023-02-08 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('World_Cup', '0007_rename_titre_foot_productfoot_titre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryfoot',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='commandefoot',
            options={'ordering': ['-date_commande']},
        ),
        migrations.AlterModelOptions(
            name='productfoot',
            options={'ordering': ['-date_added']},
        ),
        migrations.RenameField(
            model_name='categoryfoot',
            old_name='date_added_foot',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='categoryfoot',
            old_name='name_foot',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='adresse_foot',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='date_commande_foot',
            new_name='date_commande',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='email_foot',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='items_foot',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='nom_foot',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='pays_foot',
            new_name='pays',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='telephone_foot',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='total_foot',
            new_name='total',
        ),
        migrations.RenameField(
            model_name='commandefoot',
            old_name='ville_foot',
            new_name='ville',
        ),
        migrations.RenameField(
            model_name='productfoot',
            old_name='category_foot',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='productfoot',
            old_name='date_added_foot',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='productfoot',
            old_name='description_foot',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productfoot',
            old_name='image_foot',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='productfoot',
            old_name='price_foot',
            new_name='price',
        ),
    ]