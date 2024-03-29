# Generated by Django 5.0.1 on 2024-01-19 16:07

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone_number_alter_user_referral_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активный'),
        ),
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(default=users.models.generate_referral_code, max_length=6, verbose_name='инвайт-код'),
        ),
    ]
