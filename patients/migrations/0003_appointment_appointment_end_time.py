# Generated by Django 5.0.2 on 2024-03-24 23:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_rename_cost_invoice_amount_invoice_date_issued_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
