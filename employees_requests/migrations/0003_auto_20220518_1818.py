# Generated by Django 2.2.5 on 2022-05-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_requests', '0002_auto_20220518_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='overtime_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]