# Generated by Django 4.0.6 on 2022-08-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='e437ab39-56df-4b91-9f96-c7d2031b109c', primary_key=True, serialize=False),
        ),
    ]