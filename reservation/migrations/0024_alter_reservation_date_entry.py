# Generated by Django 4.0.6 on 2022-08-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0023_alter_reservation_date_entry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_entry',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
    ]
