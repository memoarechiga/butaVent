# Generated by Django 4.2.3 on 2023-07-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customuser_send_mail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
