# Generated by Django 4.1.1 on 2022-09-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("currency", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="order_number",
            field=models.IntegerField(),
        ),
    ]
