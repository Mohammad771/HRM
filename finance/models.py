from datetime import timezone
from django.utils import timezone
from django.db import models

# Create your models here.


class payrolls(models.Model):
    payroll_id = models.AutoField(max_length=24, primary_key=True)
    payroll_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    payroll_contract_id = models.ForeignKey('job_management.contracts', on_delete=models.CASCADE, related_name="+")
    payroll_net_salary = models.IntegerField()
    payroll_sign_off = models.BooleanField(default=False)
    payroll_sign_off_date = models.DateField()
    payroll_created_at = models.DateTimeField(default=timezone.now)
    payroll_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    payroll_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

class bank_account(models.Model):
    bank_account_id = models.AutoField(max_length=24, primary_key=True)
    bank_account_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    bank_account_bank_name = models.CharField(max_length=50)
    bank_account_card_holder_name = models.CharField(max_length=100)
    bank_account_iban_number = models.CharField(max_length=30)
    payroll_created_at = models.DateTimeField(default=timezone.now)
    payroll_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    payroll_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return "Bank Account " + str(self.bank_account_id)


class punishments(models.Model):
    punishment_id = models.AutoField(max_length=24, primary_key=True)
    punishment_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    punishment_amount = models.IntegerField()
    punishments_cause = models.TextField()
    punishment_created_at = models.DateTimeField(default=timezone.now)
    punishment_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    punishment_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class rewards(models.Model):
    reward_id = models.AutoField(max_length=24, primary_key=True)
    reward_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    reward_amount = models.IntegerField()
    reward_cause = models.TextField()
    reward_created_at = models.DateTimeField(default=timezone.now)
    reward_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    reward_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class accounts(models.Model):
    account_id = models.AutoField(max_length=24, primary_key=True)
    account_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    account_name = models.CharField(max_length=50)
    account_phone = models.IntegerField()
    account_email = models.CharField(max_length=50, unique=True)
    account_address = models.CharField(max_length=264)
    account_created_at = models.DateTimeField(default=timezone.now)
    account_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    account_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class allowances(models.Model):
    allowance_id = models.AutoField(max_length=24, primary_key=True)
    allowance_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    allowance_type = models.CharField(max_length=50)
    allowance_amount = models.IntegerField()
    allowance_created_at = models.DateTimeField(default=timezone.now)
    allowance_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    allowance_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return "Allownce " + str(self.allowance_id)


class allowances_and_contracts(models.Model):
    allowance_and_contract_id = models.AutoField(max_length=24, primary_key=True)
    allowance_and_contract_allowance_id = models.ForeignKey(allowances, on_delete=models.CASCADE, related_name="+")
    allowance_and_contract_contract_id = models.ForeignKey('job_management.contracts', on_delete=models.CASCADE, related_name="+")
    allowance_and_contract_created_at = models.DateTimeField(default=timezone.now)
    allowance_and_contract_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    allowance_and_contract_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class social_insurances(models.Model):
    social_insurance_id = models.AutoField(max_length=24, primary_key=True)
    social_insurance_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    social_insurance_amount = models.IntegerField()
    social_insurance_created_at = models.DateTimeField(default=timezone.now)
    social_insurance_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    social_insurance_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class annual_bonuses(models.Model):
    annual_bonus_id = models.AutoField(max_length=24, primary_key=True)
    annual_bonus_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    annual_bonus_amount = models.IntegerField()
    annual_bonus_created_at = models.DateTimeField(default=timezone.now)
    annual_bonus_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    annual_bonus_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return "Annual Bonus " + str(self.annual_bonus_id)


class incentives(models.Model):
    incentive_id = models.AutoField(max_length=24, primary_key=True)
    incentive_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    incentive_amount = models.IntegerField()
    incentive_created_at = models.DateTimeField(default=timezone.now)
    incentive_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    incentive_deleted_at = models.DateTimeField(null=True, default=None, blank=True)
