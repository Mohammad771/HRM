# Generated by Django 2.2.5 on 2022-03-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20220320_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id_number',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
