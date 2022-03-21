from django.db import models

# Create your models here.
from job_management.models import job_titles, departments
from users.models import attachments, users


class referendums(models.Model):
    referendum_id = models.AutoField(max_length=24, primary_key=True)
    referendum_attachment_id = models.ForeignKey(attachments, on_delete=models.CASCADE)
    referendum_response_job_title_id = models.ForeignKey(job_titles, on_delete=models.CASCADE, related_name="+")
    referendum_response_department_id = models.ForeignKey(departments, on_delete=models.CASCADE, related_name="+")
    referendum_see_response_department_id = models.ForeignKey(departments, on_delete=models.CASCADE, related_name="+")
    referendum_see_response_job_title_id = models.ForeignKey(job_titles, on_delete=models.CASCADE, related_name="+")
    referendum_created_by = models.ForeignKey(users, on_delete=models.CASCADE)
    referendum_subject = models.CharField(max_length=264)
    referendum_title = models.CharField(max_length=50)
    referendum_details = models.TextField()
    referendum_created_at = models.DateTimeField(default=timezone.now)
    referendum_updated_at = models.DateTimeField(null=True, default=None, blank=True)
    referendum_deleted_at = models.DateTimeField(null=True, default=None, blank=True)