# Generated by Django 5.1 on 2024-09-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_alter_teacher_phonenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phonenum',
            field=models.BigIntegerField(),
        ),
    ]
