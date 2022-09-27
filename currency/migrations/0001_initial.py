# Generated by Django 4.1.1 on 2022-09-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seq_number", models.IntegerField()),
                ("order_number", models.IntegerField(max_length=7)),
                ("price_usd", models.DecimalField(decimal_places=2, max_digits=6)),
                ("price_rub", models.DecimalField(decimal_places=2, max_digits=8)),
                ("delivery_date", models.DateField()),
            ],
        ),
    ]
