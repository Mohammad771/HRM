# Generated by Django 2.2.5 on 2022-03-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0010_delete_add_job_titles'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='department_status',
            field=models.BooleanField(default=True),
        ),
    ]
