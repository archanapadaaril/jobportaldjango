# Generated by Django 4.1.7 on 2023-05-03 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_alter_job_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_featured',
            field=models.BooleanField(null=True, verbose_name='Is Featured'),
        ),
    ]
