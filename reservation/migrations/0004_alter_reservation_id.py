# Generated by Django 4.0.6 on 2022-08-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='9f1bb496-bd54-4391-8502-34ef02b7d361', primary_key=True, serialize=False),
        ),
    ]
