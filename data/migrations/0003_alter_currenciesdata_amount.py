# Generated by Django 3.2.8 on 2021-10-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20211019_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenciesdata',
            name='amount',
            field=models.IntegerField(max_length=50),
        ),
    ]
