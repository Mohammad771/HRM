# Generated by Django 2.2.5 on 2022-03-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20220319_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id_number',
            field=models.CharField(default='8553482922', max_length=10),
        ),
    ]
