# Generated by Django 2.2.5 on 2022-05-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_auto_20220530_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='payrolls',
            name='payroll_confirmation',
            field=models.CharField(default='1', max_length=60),
            preserve_default=False,
        ),
    ]
