# Generated by Django 4.2.6 on 2023-10-27 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Osoba', '0002_osoba_data_dodania_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko']},
        ),
    ]