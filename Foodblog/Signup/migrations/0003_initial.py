# Generated by Django 4.0.1 on 2022-02-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Signup', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('contraseña', models.CharField(max_length=40)),
            ],
        ),
    ]