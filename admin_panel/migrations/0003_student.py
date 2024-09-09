# Generated by Django 5.1 on 2024-09-02 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('phonenum', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('degree', models.CharField(max_length=300)),
                ('college', models.CharField(max_length=250)),
                ('totalamount', models.IntegerField()),
                ('paidamount', models.IntegerField()),
                ('dueamount', models.FloatField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.course')),
            ],
        ),
    ]
