# Generated by Django 4.1.7 on 2023-02-21 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_report', '0006_alter_storereport_store_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storestatus',
            old_name='timestamp_utc',
            new_name='timestamp',
        ),
    ]
