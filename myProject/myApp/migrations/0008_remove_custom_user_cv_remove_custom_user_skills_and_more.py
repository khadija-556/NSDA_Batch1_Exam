# Generated by Django 5.0 on 2023-12-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_custom_user_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='jobapply_m',
            name='Candit_cv',
        ),
        migrations.RemoveField(
            model_name='jobapply_m',
            name='applyDate',
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='cv',
            field=models.FileField(null=True, upload_to='media/cv'),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='skills',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
