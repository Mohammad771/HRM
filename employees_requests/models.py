from datetime import timezone
from django.utils import timezone
from django.db import models

# Create your models here.

class vacations(models.Model):
    vacation_id = models.AutoField(max_length=24, primary_key=True)
    vacation_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    vacation_leaving_date = models.DateField()
    vacation_coming_date = models.DateField()
    vacation_is_paid = models.BooleanField()
    vacation_created_at = models.DateTimeField(default=timezone.now)
    vacation_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    vacation_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class loans(models.Model):
    loan_id = models.AutoField(max_length=24, primary_key=True)
    loan_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    # loan_type = models.CharField(max_length=24)
    loan_amount = models.IntegerField()
    loan_started_date = models.DateField()
    loan_period = models.IntegerField()
    loan_number_of_complete_payment = models.IntegerField(null=True, default=0)
    loan_status = models.BooleanField(null=True, default=False)
    loan_is_approved = models.BooleanField(null=True, default=False)
    loan_created_at = models.DateTimeField(default=timezone.now)
    loan_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    loan_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return "Loan " + str(self.loan_id)

class overtime_types(models.Model):
    overtime_type_id = models.AutoField(max_length=24, primary_key=True)
    overtime_type_name = models.CharField(max_length=50)
    overtime_type_created_at = models.DateTimeField(default=timezone.now)
    overtime_type_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    overtime_type_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class overtime(models.Model):
    overtime_id = models.AutoField(max_length=24, primary_key=True)
    overtime_overtime_type_id = models.ForeignKey(overtime_types, on_delete=models.CASCADE, related_name="+")
    overtime_status = models.BooleanField()
    overtime_hours = models.IntegerField()
    overtime_amount = models.IntegerField()
    overtime_created_at = models.DateTimeField(default=timezone.now)
    overtime_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    overtime_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class complains_and_suggestions(models.Model):
    complains_and_suggestions_id = models.AutoField(max_length=24, primary_key=True)
    complains_and_suggestions_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    complains_or_suggestions = models.BooleanField()
    complains_and_suggestions_text = models.TextField
    complains_and_suggestions_created_at = models.DateTimeField(default=timezone.now)
    complains_and_suggestions_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    complains_and_suggestions_deleted_at = models.DateTimeField(null=True, default=None, blank=True)