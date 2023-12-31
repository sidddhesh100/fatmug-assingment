# Generated by Django 4.2.7 on 2023-12-05 17:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VendorModel",
            fields=[
                ("vendor_code", models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ("contact_details", models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ("address", models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(15)])),
                (
                    "on_time_delivery_rate",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                (
                    "quality_rating_avg",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                (
                    "average_response_time",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                (
                    "fulfillment_rate",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
            ],
            options={
                "db_table": "vendor",
            },
        ),
        migrations.CreateModel(
            name="PerformanceModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "on_time_delivery_rate",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                (
                    "quality_rating_avg",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                (
                    "average_response_time",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                (
                    "fulfillment_rate",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)],
                    ),
                ),
                ("vendor", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="vendor.vendormodel")),
            ],
            options={
                "db_table": "performance",
            },
        ),
    ]
