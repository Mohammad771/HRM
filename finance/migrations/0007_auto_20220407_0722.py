# Generated by Django 2.2.5 on 2022-04-07 04:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20220407_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='punishments',
            name='evaluation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rewards',
            name='evaluation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
