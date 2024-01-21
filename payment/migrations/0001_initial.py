# Generated by Django 5.0.1 on 2024-01-21 09:04

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_alter_lesson_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pay', models.DateTimeField(default=datetime.datetime.now, verbose_name='дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='сумма')),
                ('pay_type', models.CharField(choices=[('card', 'перевод'), ('cash', 'наличные')], default='card', max_length=4, verbose_name='способ оплаты')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.course', verbose_name='курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.lesson', verbose_name='урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]
