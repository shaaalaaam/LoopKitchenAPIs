# Generated by Django 4.1.7 on 2023-02-18 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreTimezone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.IntegerField()),
                ('timezone_str', models.CharField(default='America/Chicago', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StoreStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp_utc', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_report.storetimezone')),
            ],
        ),
        migrations.CreateModel(
            name='StoreHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField()),
                ('start_time_local', models.TimeField()),
                ('end_time_local', models.TimeField()),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_report.storetimezone')),
            ],
        ),
    ]