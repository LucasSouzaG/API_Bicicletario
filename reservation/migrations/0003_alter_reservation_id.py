# Generated by Django 4.0.6 on 2022-08-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='fb106d4c-9926-4bc7-a430-e16acf5a726a', primary_key=True, serialize=False),
        ),
    ]
