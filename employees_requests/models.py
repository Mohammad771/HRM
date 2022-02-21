from django.db import models

# Create your models here.

class vacations(models.Model):
    vacation_id = models.AutoField(max_length=24, primary_key=True)
    vacation_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    vacation_leaving_date = models.DateField()
    vacation_coming_date = models.DateField()
    vacation_is_paid = models.BooleanField()
    vacation_created_at = models.DateTimeField()
    vacation_updated_at = models.DateTimeField()
    vacation_deleted_at = models.DateTimeField()


class loans(models.Model):
    loan_id = models.AutoField(max_length=24, primary_key=True)
    loan_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    loan_type = models.CharField(max_length=24)
    loan_amount = models.IntegerField()
    loan_started_date = models.DateField()
    loan_period = models.IntegerField()
    loan_number_of_complete_payment = models.IntegerField()
    loan_status = models.BooleanField()
    loan_admin_approval = models.BooleanField()
    loan_created_at = models.DateTimeField()
    loan_updated_at = models.DateTimeField()
    loan_deleted_at = models.DateTimeField()


class overtime_types(models.Model):
    overtime_type_id = models.AutoField(max_length=24, primary_key=True)
    overtime_type_name = models.CharField(max_length=50)
    overtime_type_created_at = models.DateTimeField()
    overtime_type_updated_at = models.DateTimeField()
    overtime_type_deleted_at = models.DateTimeField()


class overtime(models.Model):
    overtime_id = models.AutoField(max_length=24, primary_key=True)
    overtime_overtime_type_id = models.ForeignKey(overtime_types, on_delete=models.CASCADE, related_name="+")
    overtime_status = models.BooleanField()
    overtime_hours = models.IntegerField()
    overtime_amount = models.IntegerField()
    overtime_created_at = models.DateTimeField()
    overtime_updated_at = models.DateTimeField()
    overtime_deleted_at = models.DateTimeField()


class complains_and_suggestions(models.Model):
    complains_and_suggestions_id = models.AutoField(max_length=24, primary_key=True)
    complains_and_suggestions_user_id = models.ForeignKey('users.users', on_delete=models.CASCADE, related_name="+")
    complains_or_suggestions = models.BooleanField()
    complains_and_suggestions_text = models.TextField
    complains_and_suggestions_created_at = models.DateTimeField()
    complains_and_suggestions_updated_at = models.DateTimeField()
    complains_and_suggestions_deleted_at = models.DateTimeField()