# Generated by Django 4.1.7 on 2023-02-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_report', '0005_alter_storereport_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storereport',
            name='store_id',
            field=models.IntegerField(default=0),
        ),
    ]
