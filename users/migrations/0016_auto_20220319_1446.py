# Generated by Django 2.2.5 on 2022-03-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20220319_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id_number',
            field=models.CharField(default='2222009897', max_length=10),
        ),
    ]
