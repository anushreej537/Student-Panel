# Generated by Django 5.1.1 on 2024-09-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0008_alter_student_phonenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
