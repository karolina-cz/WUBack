# Generated by Django 3.1.4 on 2020-12-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wu_user',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]
