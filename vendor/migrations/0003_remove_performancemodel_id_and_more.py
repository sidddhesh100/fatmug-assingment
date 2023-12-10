# Generated by Django 4.2.7 on 2023-12-07 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendormodel_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancemodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='performancemodel',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='vendor.vendormodel'),
        ),
    ]
