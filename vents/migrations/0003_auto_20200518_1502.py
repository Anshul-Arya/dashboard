# Generated by Django 3.0.6 on 2020-05-18 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vents', '0002_auto_20200518_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vent_availability',
            name='Predicted_Vent_Shortage_in_14days',
            field=models.CharField(max_length=4),
        ),
    ]