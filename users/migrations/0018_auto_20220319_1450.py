# Generated by Django 2.2.5 on 2022-03-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20220319_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id_number',
            field=models.CharField(default='2224724235', max_length=10),
        ),
    ]
