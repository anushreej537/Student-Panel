# Generated by Django 5.1 on 2024-09-10 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_alter_teacher_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phonenum',
            field=models.CharField(max_length=20),
        ),
    ]
