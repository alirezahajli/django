# Generated by Django 3.2.8 on 2021-10-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_currenciesdata_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenciesdata',
            name='currency',
            field=models.CharField(choices=[('USD', 1), ('EURO', 2)], default=1, max_length=100),
        ),
    ]
