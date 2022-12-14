# Generated by Django 4.0.6 on 2022-08-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0016_alter_reservation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='bike_model',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='date_entry',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='date_output',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='number_allocation',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='06b26a9a-f49e-4f72-ba3c-a7f34e00a28e', primary_key=True, serialize=False),
        ),
    ]
