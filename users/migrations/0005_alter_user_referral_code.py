# Generated by Django 5.0.1 on 2024-01-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_phone_number_alter_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(default='DTITJ1', max_length=6, verbose_name='инвайт-код'),
        ),
    ]
