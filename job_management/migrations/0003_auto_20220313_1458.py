# Generated by Django 2.2.5 on 2022-03-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0002_auto_20220312_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='department_created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
