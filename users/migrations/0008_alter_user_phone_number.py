# Generated by Django 5.0.1 on 2024-01-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_username_alter_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True, verbose_name='номер телефона'),
        ),
    ]
