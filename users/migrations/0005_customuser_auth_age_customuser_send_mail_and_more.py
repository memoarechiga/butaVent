# Generated by Django 4.2.3 on 2023-07-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_city_customuser_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='auth_age',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='send_mail',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='terms_conds',
            field=models.BooleanField(null=True),
        ),
    ]
