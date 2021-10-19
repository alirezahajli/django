# Generated by Django 3.2.8 on 2021-10-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrenciesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
