# Generated by Django 4.0.1 on 2022-02-21 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_campo1_user_contraseña_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]