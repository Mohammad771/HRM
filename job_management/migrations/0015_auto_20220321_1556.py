# Generated by Django 2.2.5 on 2022-03-21 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0014_auto_20220320_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contracts',
            name='contract_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='contract_deleted_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='contracts',
            name='contract_updated_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
