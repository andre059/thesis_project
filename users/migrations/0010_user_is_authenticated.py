# Generated by Django 5.0.1 on 2024-01-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_is_authorized'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_authenticated',
            field=models.BooleanField(default=False, verbose_name='Пользователь аутентифицирован'),
        ),
    ]