# Generated by Django 4.2.7 on 2023-12-05 17:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('po_number', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete'), ('Cancelled', 'Cancelled')], max_length=9)),
                ('quality_rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('issue_date', models.DateTimeField(null=True)),
                ('acknowledgment_date', models.DateTimeField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vendor.vendormodel')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
