# Generated by Django 2.2.5 on 2022-06-08 15:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('track_performance', '0015_remove_evaluations_evaluation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluations',
            name='evaluation_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
