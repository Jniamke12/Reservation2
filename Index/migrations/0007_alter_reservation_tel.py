# Generated by Django 5.1.2 on 2024-11-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_reservation_status_alter_reservation_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
