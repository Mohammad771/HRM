from datetime import timezone
from django.utils import timezone
from django.db import models

# Create your models here.
from job_management.models import job_titles, departments
from users.models import users


class events(models.Model):
    event_id = models.AutoField(max_length=24, primary_key=True)
    event_created_by = models.ForeignKey(users, on_delete=models.CASCADE, related_name="+")
    event_job_title_id = models.ForeignKey(job_titles, on_delete=models.CASCADE, related_name="+")
    event_department_id = models.ForeignKey(departments, on_delete=models.CASCADE, related_name="+")
    event_type = models.CharField(max_length=30)
    event_title = models.CharField(max_length=50)
    event_date = models.DateField()
    event_location = models.CharField(max_length=50)
    event_created_at = models.DateTimeField(default=timezone.now)
    event_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    event_deleted_at = models.DateTimeField(null=True, default=None, blank=True)