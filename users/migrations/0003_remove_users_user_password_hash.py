# Generated by Django 2.2.5 on 2022-03-07 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220307_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_password_hash',
        ),
    ]
