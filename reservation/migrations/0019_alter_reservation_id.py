# Generated by Django 4.0.6 on 2022-08-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0018_reservation_bike_model_reservation_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='8d4dded0-9f10-48e8-9897-172b5f762252', primary_key=True, serialize=False),
        ),
    ]
