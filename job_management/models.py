from django.db import models

# Create your models here.
from finance.models import accounts


class departments(models.Model):
    department_id = models.AutoField(max_length=24, primary_key=True)
    department_name = models.CharField(max_length=50)
    department_created_at = models.DateTimeField()
    department_updated_at = models.DateTimeField()
    department_deleted_at = models.DateTimeField()


class job_titles(models.Model):
    job_title_id = models.AutoField(max_length=24, primary_key=True)
    job_title_department_id = models.ForeignKey(departments, on_delete=models.CASCADE, related_name="+")
    job_title_location = models.ForeignKey(departments, on_delete=models.CASCADE, related_name="+")
    job_title_code = models.IntegerField()
    job_title_description = models.TextField(blank=True, null=True)
    job_title_qualification = models.TextField(blank=True, null=True)
    job_title_opening_position = models.CharField(max_length=264)
    job_title_hour_price = models.IntegerField()
    job_title_overtime_percentage = models.IntegerField()
    job_title_available_online = models.BooleanField()
    job_title_days_off = models.IntegerField()
    job_title_status = models.BooleanField()
    job_title_created_at = models.DateTimeField()
    job_title_updated_at = models.DateTimeField()
    job_title_deleted_at = models.DateTimeField()


class job_locations(models.Model):
    job_locations_id = models.AutoField(max_length=24, primary_key=True)
    job_locations_name = models.CharField(max_length=50)
    job_locations_description = models.TextField(blank=True, null=True)
    job_locations_created_at = models.DateTimeField()
    job_locations_updated_at = models.DateTimeField()
    job_locations_deleted_at = models.DateTimeField()


class contracts(models.Model):
    contract_id = models.AutoField(max_length=24, primary_key=True)
    contract_account_id = models.ForeignKey(accounts, on_delete=models.CASCADE, related_name="+")
    contract_status = models.BooleanField()
    contract_hour_price = models.IntegerField()
    contract_has_trail_period = models.BooleanField()
    contract_expiry_date = models.DateField()
    contract_date_of_performing = models.DateField
    contract_approval = models.BooleanField()
    contract_conditions = models.TextField(blank=True, null=True)
    contract_created_at = models.DateTimeField()
    contract_updated_at = models.DateTimeField()
    contract_deleted_at = models.DateTimeField()