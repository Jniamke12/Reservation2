# Generated by Django 5.1.3 on 2024-11-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0008_table_remove_reservation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='number',
            field=models.IntegerField(),
        ),
    ]
