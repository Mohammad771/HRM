# Generated by Django 2.2.5 on 2022-03-12 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20220312_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_DOB',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
    ]
