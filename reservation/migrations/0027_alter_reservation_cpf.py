# Generated by Django 4.0.6 on 2022-08-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0026_alter_reservation_date_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='cpf',
            field=models.CharField(max_length=255),
        ),
    ]
