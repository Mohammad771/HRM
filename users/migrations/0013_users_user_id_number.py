# Generated by Django 2.2.5 on 2022-03-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20220312_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_id_number',
            field=models.CharField(default='4283432934', max_length=10),
        ),
    ]
