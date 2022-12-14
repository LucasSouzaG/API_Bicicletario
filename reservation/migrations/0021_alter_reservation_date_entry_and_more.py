# Generated by Django 4.0.6 on 2022-08-24 18:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0020_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_entry',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_output',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
