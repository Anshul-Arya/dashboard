# Generated by Django 3.0.6 on 2020-05-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vents', '0003_auto_20200518_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vent_availability',
            name='Available_Vents',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vent_availability',
            name='Predicted_Vent_Shortage_in_14days',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='vent_availability',
            name='Total_Vents',
            field=models.IntegerField(),
        ),
    ]
