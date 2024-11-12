# Generated by Django 5.1.2 on 2024-11-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_reservation_status_alter_reservation_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='status',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='tel',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]