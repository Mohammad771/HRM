# Generated by Django 2.2.5 on 2022-06-08 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20220608_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_nationality_ID',
            field=models.CharField(max_length=13),
        ),
    ]
