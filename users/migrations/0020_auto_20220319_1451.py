# Generated by Django 2.2.5 on 2022-03-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20220319_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id_number',
            field=models.CharField(default='6341938033', max_length=10),
        ),
    ]
