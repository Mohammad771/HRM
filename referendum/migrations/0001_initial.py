# Generated by Django 2.2.5 on 2022-02-21 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_management', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='referendums',
            fields=[
                ('referendum_id', models.AutoField(max_length=24, primary_key=True, serialize=False)),
                ('referendum_subject', models.CharField(max_length=264)),
                ('referendum_title', models.CharField(max_length=50)),
                ('referendum_details', models.TextField()),
                ('referendum_created_at', models.DateTimeField()),
                ('referendum_updated_at', models.DateTimeField()),
                ('referendum_deleted_at', models.DateTimeField()),
                ('referendum_attachment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.attachments')),
                ('referendum_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
                ('referendum_response_department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.departments')),
                ('referendum_response_job_title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.job_titles')),
                ('referendum_see_response_department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.departments')),
                ('referendum_see_response_job_title_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='job_management.job_titles')),
            ],
        ),
    ]
