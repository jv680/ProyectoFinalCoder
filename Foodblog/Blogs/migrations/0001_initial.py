# Generated by Django 4.0.1 on 2022-02-21 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('categoría', models.CharField(max_length=40)),
                ('ingredientes', models.CharField(max_length=2000)),
                ('preparación', models.CharField(max_length=2000)),
            ],
        ),
    ]