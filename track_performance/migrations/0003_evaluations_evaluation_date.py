# Generated by Django 2.2.5 on 2022-03-21 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('track_performance', '0002_auto_20220321_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluations',
            name='evaluation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
