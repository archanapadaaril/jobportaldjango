# Generated by Django 4.1.7 on 2023-05-03 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_remove_jobdetails_job_title_jobdetails_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(null=True, verbose_name='Is Active'),
        ),
    ]
