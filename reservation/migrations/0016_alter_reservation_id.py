# Generated by Django 4.0.6 on 2022-08-02 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0015_alter_reservation_bike_model_alter_reservation_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='b55e87a4-b5ea-469d-8658-18010c346dd0', primary_key=True, serialize=False),
        ),
    ]
