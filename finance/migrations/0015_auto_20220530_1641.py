# Generated by Django 2.2.5 on 2022-05-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0014_payrolls_payroll_sign_off_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payrolls',
            name='payroll_sign_off_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
