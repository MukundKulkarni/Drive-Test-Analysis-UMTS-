# Generated by Django 2.2.8 on 2020-02-24 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinterface', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivetestdata',
            name='filename',
            field=models.CharField(max_length=255),
        ),
    ]
