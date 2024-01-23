# Generated by Django 5.0.1 on 2024-01-23 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRateRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('usd_to_rub_rate', models.FloatField()),
            ],
        ),
    ]
