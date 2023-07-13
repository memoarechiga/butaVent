# Generated by Django 4.2.3 on 2023-07-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='auth_age',
            field=models.CharField(blank=True, default='False', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='send_mail',
            field=models.CharField(blank=True, default='False', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='terms_conds',
            field=models.CharField(blank=True, default='False', max_length=50, null=True),
        ),
    ]