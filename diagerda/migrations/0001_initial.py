# Generated by Django 5.0.3 on 2024-03-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='дата и время приема')),
            ],
            options={
                'verbose_name': 'запись на диагностику',
                'verbose_name_plural': 'записи на диагностику',
            },
        ),
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('price', models.PositiveIntegerField(verbose_name='стоимость')),
            ],
            options={
                'verbose_name': 'диагностика',
                'verbose_name_plural': 'диагностики',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='person/', verbose_name='Фото')),
                ('speciality', models.CharField(max_length=50, verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'врач',
                'verbose_name_plural': 'врачи',
            },
        ),
    ]