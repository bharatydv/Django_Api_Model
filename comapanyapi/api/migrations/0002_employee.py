# Generated by Django 5.0.3 on 2024-03-07 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('Phones', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'female'), ('other', 'Other')], max_length=6)),
                ('address', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('developer', 'developer'), ('Project Leader', 'PL')], max_length=15)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
