# Generated by Django 2.2.5 on 2022-03-21 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track_performance', '0003_evaluations_evaluation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluations',
            name='evaluation_department_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='job_management.departments'),
        ),
        migrations.AlterField(
            model_name='evaluations',
            name='evaluation_job_title_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='job_management.job_titles'),
        ),
        migrations.AlterField(
            model_name='evaluations',
            name='evaluation_user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
