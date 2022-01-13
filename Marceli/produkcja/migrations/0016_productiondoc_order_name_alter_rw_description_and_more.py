# Generated by Django 4.0.1 on 2022-01-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkcja', '0015_productiondoc_number_productiondoc_rw_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productiondoc',
            name='order_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='rw',
            name='description',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='rw',
            name='fakturownia_id',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]