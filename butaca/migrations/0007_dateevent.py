# Generated by Django 4.2.3 on 2023-07-19 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('butaca', '0006_remove_event_date1_remove_event_date2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('draw_event', models.DateField(null=True)),
                ('draw_limit_date', models.DateField(null=True)),
                ('event_time', models.TimeField(null=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='butaca.event')),
            ],
        ),
    ]
