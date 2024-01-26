# Generated by Django 5.0 on 2023-12-27 15:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_remove_custom_user_cv_remove_custom_user_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseekerprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobseekerprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]