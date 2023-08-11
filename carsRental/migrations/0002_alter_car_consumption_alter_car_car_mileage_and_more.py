# Generated by Django 4.2.4 on 2023-08-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsRental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Consumption',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_mileage',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='car',
            name='cars_type',
            field=models.CharField(choices=[('Shooting brake', 'Shooting brake'), ('Suv', 'Suv'), ('Kombi', 'Kombi'), ('Van', 'Van'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Sedan', 'Sedan')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='deposit',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(choices=[('Petrol', 'Benzyna'), ('Electric', 'Elektryczny'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybryda')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_gears',
            field=models.CharField(choices=[('6', '6'), ('7', '7'), ('5', '5'), ('8', '8')], max_length=8),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Manual', 'Manualna'), ('Automatic', 'Automatyczna')], max_length=32),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.CharField(max_length=8),
        ),
    ]