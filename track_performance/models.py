##NO EDIT HERE
from datetime import timezone

from django.db import models
from users.models import users


# Create your models here.

class evaluations(models.Model):
    evaluation_id = models.AutoField(max_length=24, primary_key=True)
    evaluation_user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    evaluation_interaction_rate = models.IntegerField()
    evaluation_time_rate = models.IntegerField()
    evaluation_quality_rate = models.IntegerField()
    evaluation_created_at = models.DateTimeField(default=timezone.now)
    evaluation_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    evaluation_deleted_at = models.DateTimeField(null=True, default=None, blank=True)


class attendance(models.Model):
    attendance_id = models.AutoField(max_length=24, primary_key=True)
    attendance_user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name="+")
    attendance_date = models.DateField
    attendance_clock_in = models.DateTimeField()
    attendance_clock_out = models.DateTimeField()
    attendance_total_hours = models.IntegerField()
    attendance_half_day = models.BooleanField()
    attendance_working_from = models.CharField(max_length=24)
    attendance_created_at = models.DateTimeField(default=timezone.now)
    attendance_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    attendance_deleted_at = models.DateTimeField(null=True, default=None, blank=True)