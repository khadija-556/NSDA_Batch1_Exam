# Generated by Django 5.0 on 2023-12-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_job_m_company_logo_job_m_deadline_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_m',
            name='deadline',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]