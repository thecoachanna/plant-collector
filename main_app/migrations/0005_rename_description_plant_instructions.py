# Generated by Django 4.1.7 on 2023-03-11 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_plant_description_alter_plant_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='description',
            new_name='instructions',
        ),
    ]
