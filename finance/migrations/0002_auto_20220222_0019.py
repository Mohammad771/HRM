# Generated by Django 2.2.5 on 2022-02-21 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance', '0001_initial'),
        ('job_management', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_insurances',
            name='social_insurance_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='rewards',
            name='reward_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='punishments',
            name='punishment_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='payrolls',
            name='payroll_contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.contracts'),
        ),
        migrations.AddField(
            model_name='payrolls',
            name='payroll_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='incentives',
            name='incentive_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='annual_bounces',
            name='annual_bounce_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='allowances_and_contracts',
            name='allowance_and_contract_allowance_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='finance.allowances'),
        ),
        migrations.AddField(
            model_name='allowances_and_contracts',
            name='allowance_and_contract_contract_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.contracts'),
        ),
        migrations.AddField(
            model_name='allowances',
            name='allowance_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='account_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='users.users'),
        ),
    ]
