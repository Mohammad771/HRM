# Generated by Django 2.2.5 on 2022-03-08 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220307_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_middle_name',
        ),
    ]
