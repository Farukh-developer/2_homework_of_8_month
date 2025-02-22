# Generated by Django 5.0.6 on 2024-07-01 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('parents_phone_num', models.IntegerField()),
                ('telegram_link', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=12)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.courses')),
                ('teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.teachers')),
            ],
        ),
    ]
