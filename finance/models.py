from django.db import models

# Create your models here.


class payrolls(models.Model):
    payroll_id = models.AutoField(max_length=24, primary_key=True)
    payroll_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    payroll_contract_id = models.ForeignKey('job_management.contracts', on_delete=models.CASCADE, related_name="+")
    payroll_net_salary = models.IntegerField()
    payroll_sign_off = models.BooleanField(default=False)
    payroll_sign_off_date = models.DateField()
    payroll_created_at = models.DateTimeField()
    payroll_updated_at = models.DateTimeField()
    payroll_deleted_at = models.DateTimeField()


class punishments(models.Model):
    punishment_id = models.AutoField(max_length=24, primary_key=True)
    punishment_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    punishment_amount = models.IntegerField()
    punishments_cause = models.TextField()
    punishment_created_at = models.DateTimeField()
    punishment_updated_at = models.DateTimeField()
    punishment_deleted_at = models.DateTimeField()


class rewards(models.Model):
    reward_id = models.AutoField(max_length=24, primary_key=True)
    reward_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    reward_amount = models.IntegerField()
    reward_cause = models.TextField()
    reward_created_at = models.DateTimeField()
    reward_updated_at = models.DateTimeField()
    reward_deleted_at = models.DateTimeField()


class accounts(models.Model):
    account_id = models.AutoField(max_length=24, primary_key=True)
    account_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    account_name = models.CharField(max_length=50)
    account_phone = models.IntegerField()
    account_email = models.CharField(max_length=50, unique=True)
    account_address = models.CharField(max_length=264)
    account_created_at = models.DateTimeField()
    account_updated_at = models.DateTimeField()
    account_deleted_at = models.DateTimeField()


class allowances(models.Model):
    allowance_id = models.AutoField(max_length=24, primary_key=True)
    allowance_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    allowance_type = models.CharField(max_length=50)
    allowance_amount = models.IntegerField()
    allowance_created_at = models.DateTimeField()
    allowance_updated_at = models.DateTimeField()
    allowance_deleted_at = models.DateTimeField()


class allowances_and_contracts(models.Model):
    allowance_and_contract_id = models.AutoField(max_length=24, primary_key=True)
    allowance_and_contract_allowance_id = models.ForeignKey(allowances, on_delete=models.CASCADE, related_name="+")
    allowance_and_contract_contract_id = models.ForeignKey('job_management.contracts', on_delete=models.CASCADE, related_name="+")
    allowance_and_contract_created_at = models.DateTimeField()
    allowance_and_contract_updated_at = models.DateTimeField()
    allowance_and_contract_deleted_at = models.DateTimeField()


class social_insurances(models.Model):
    social_insurance_id = models.AutoField(max_length=24, primary_key=True)
    social_insurance_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    social_insurance_amount = models.IntegerField()
    social_insurance_created_at = models.DateTimeField()
    social_insurance_updated_at = models.DateTimeField()
    social_insurance_deleted_at = models.DateTimeField()


class annual_bounces(models.Model):
    annual_bounce_id = models.AutoField(max_length=24, primary_key=True)
    annual_bounce_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    annual_bounce_amount = models.IntegerField()
    annual_bounce_created_at = models.DateTimeField()
    annual_bounce_updated_at = models.DateTimeField()
    annual_bounce_deleted_at = models.DateTimeField()


class incentives(models.Model):
    incentive_id = models.AutoField(max_length=24, primary_key=True)
    incentive_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    incentive_amount = models.IntegerField()
    incentive_created_at = models.DateTimeField()
    incentive_updated_at = models.DateTimeField()
    incentive_deleted_at = models.DateTimeField()
