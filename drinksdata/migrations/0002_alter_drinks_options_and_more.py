# Generated by Django 5.1.1 on 2025-02-18 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinksdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drinks',
            options={'verbose_name_plural': 'Drinks'},
        ),
        migrations.RenameField(
            model_name='drinks',
            old_name='description',
            new_name='flavour',
        ),
    ]
