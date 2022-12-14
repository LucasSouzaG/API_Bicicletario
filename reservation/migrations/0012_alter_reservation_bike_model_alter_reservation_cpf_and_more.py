# Generated by Django 4.0.6 on 2022-08-02 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='bike_model',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_entry',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_output',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default='33ba1136-854a-4dba-878f-254f6a08113e', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_allocation',
            field=models.IntegerField(null=True),
        ),
    ]
