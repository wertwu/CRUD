# Generated by Django 4.0 on 2021-12-23 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Ключ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Токен_аутентификации', to='auth.user', verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Токен',
                'verbose_name_plural': 'Токены',
            },
        ),
    ]