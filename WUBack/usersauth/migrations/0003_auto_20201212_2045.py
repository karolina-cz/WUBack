# Generated by Django 3.1.4 on 2020-12-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersauth', '0002_wu_user_is_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wu_user',
            name='code',
            field=models.CharField(max_length=151, null=True),
        ),
    ]
