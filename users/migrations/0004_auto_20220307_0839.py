# Generated by Django 2.2.5 on 2022-03-07 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_users_user_password_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_DOB',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_mobile',
            field=models.CharField(default='320482', max_length=15, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_nationality_ID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
