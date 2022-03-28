##NO EDIT HERE
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.db import models
from users.models import users
from job_management.models import departments, job_titles


# Create your models here.

class evaluations(models.Model):
    evaluation_id = models.AutoField(max_length=24, primary_key=True)
    evaluation_user_id = models.ForeignKey(users, on_delete=models.CASCADE, null = True, default=None, blank=True)
    evaluation_department_id = models.ForeignKey(departments, on_delete=models.CASCADE, null = True, default=None, blank=True)
    evaluation_job_title_id = models.ForeignKey(job_titles, on_delete=models.CASCADE, null = True, default=None, blank=True)
    evaluation_interaction_rate = models.IntegerField()
    evaluation_time_rate = models.IntegerField()
    evaluation_quality_rate = models.IntegerField()
    evaluation_overall_rate = models.IntegerField()
    evaluation_date = models.DateField()
    evaluation_created_at = models.DateTimeField(auto_now=True)
    evaluation_updated_at = models.DateTimeField(null = True, default=None, blank=True)
    evaluation_deleted_at = models.DateTimeField(null = True, default=None, blank=True)

    def __str__(self):
        if self.evaluation_user_id:
            return str(self.evaluation_user_id) + " (User)"
        elif self.evaluation_department_id:
            return str(self.evaluation_department_id) + " (Deaprtment)"
        elif self.evaluation_job_title_id:
            return str(self.evaluation_job_title_id) + " (Job Title)"
        else:
            return str(self.evaluation_id)

class attendance_file(models.Model):
    attendance_file_id = models.AutoField(max_length=24, primary_key=True)
    attendance_file = models.FileField(upload_to='static/upload/attendance_files', validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])
    attendance_file_date = models.DateField()
    attendance_file_created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Attendance Sheet: " + str(self.attendance_file_date)

class attendance(models.Model):
    attendance_id = models.AutoField(max_length=24, primary_key=True)
    attendance_source_file_id = models.ForeignKey(attendance_file, on_delete=models.CASCADE, null=True, default=None, blank=True)
    attendance_user_id = models.ForeignKey(users, on_delete=models.CASCADE, related_name="+")
    attendance_date = models.DateField()
    attendance_clock_in = models.TimeField()
    attendance_clock_out = models.TimeField()
    attendance_duration = models.TimeField()
    attendance_half_day = models.BooleanField(null=True, default=None, blank=True)
    attendance_working_from = models.CharField(max_length=24)
    attendance_created_at = models.DateTimeField(default=timezone.now)
    attendance_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    attendance_deleted_at = models.DateTimeField(null=True, default=None, blank=True)




    