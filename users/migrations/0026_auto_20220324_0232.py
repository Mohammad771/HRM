# Generated by Django 2.2.5 on 2022-03-23 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0016_auto_20220324_0232'),
        ('users', '0025_auto_20220321_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_education_degree',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_experience_years',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='user_job_title_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.job_titles'),
        ),
    ]
