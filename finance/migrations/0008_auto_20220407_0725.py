# Generated by Django 2.2.5 on 2022-04-07 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20220407_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewards',
            name='reward_cause',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
