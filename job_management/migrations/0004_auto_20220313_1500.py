# Generated by Django 2.2.5 on 2022-03-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0003_auto_20220313_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='department_deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='departments',
            name='department_updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
