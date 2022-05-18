from datetime import timezone
from django.utils import timezone
from django.db import models
import datetime
from django.core.exceptions import ValidationError

# Create your models here.

class vacations(models.Model):
    vacation_id = models.AutoField(max_length=24, primary_key=True)
    vacation_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    vacation_leaving_date = models.DateField()
    vacation_coming_date = models.DateField()
    vacation_is_paid = models.BooleanField()
    vacation_is_approved = models.BooleanField(null=True, default=False, blank=True)
    vacation_created_at = models.DateTimeField(default=timezone.now)
    vacation_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    vacation_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def clean(self):
        leaving_date = self.vacation_leaving_date
        returning_date = self.vacation_coming_date
        if not (leaving_date and returning_date):
            return
        time_difference = returning_date - leaving_date
        if time_difference.days < 0:
            raise ValidationError(
                {'vacation_coming_date': "vacations's returning date cannot be before leaving date"})

    def __str__(self):
        return str(self.vacation_user_id) + "'s vacation " + str(self.vacation_id)


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

class overtime_categories(models.Model):
    overtime_category_id = models.AutoField(max_length=24, primary_key=True)
    overtime_category_name = models.CharField(max_length=50)
    overtime_category_created_at = models.DateTimeField(default=timezone.now)
    overtime_category_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    overtime_category_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return self.overtime_category_name

class overtime(models.Model):
    overtime_id = models.AutoField(max_length=24, primary_key=True)
    overtime_overtime_category_id = models.ForeignKey(overtime_categories, on_delete=models.CASCADE, related_name="+")
    overtime_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    overtime_status = models.BooleanField(null=True, default=False)
    overtime_hours = models.IntegerField()
    # overtime_amount = models.IntegerField() what's the difference between amount and hours?
    overtime_date = models.DateField()
    overtime_created_at = models.DateTimeField(default=timezone.now)
    overtime_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    overtime_deleted_at = models.DateTimeField(null=True, default=None, blank=True)

    def __str__(self):
        return "overtime " + str(self.overtime_id)

    def clean(self):
        overtime_date = self.overtime_date
        if not overtime_date:
            return
        today = datetime.date.today()
        time_difference = today - overtime_date
        if time_difference.days < -30:
            raise ValidationError(
                {'overtime_date': "overtime's date should be within 30 days from now"})
        elif time_difference.days > 0:
            raise ValidationError(
                {'overtime_date': "overtime's date cannot be in the past"})

        overtime_hours = self.overtime_hours
        print(overtime_hours)
        if overtime_hours == None:
            return
        if overtime_hours > 8:
            raise ValidationError(
                {'overtime_hours': "overtime's hours cannot exceed 8"})
        elif overtime_hours < 1:
            raise ValidationError(
                {'overtime_hours': "overtime's hours cannot be less than 1"})

class complains_and_suggestions(models.Model):
    complains_and_suggestions_id = models.AutoField(max_length=24, primary_key=True)
    complains_and_suggestions_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    complains_or_suggestions = models.BooleanField()
    complains_and_suggestions_text = models.TextField
    complains_and_suggestions_created_at = models.DateTimeField(default=timezone.now)
    complains_and_suggestions_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    complains_and_suggestions_deleted_at = models.DateTimeField(null=True, default=None, blank=True)