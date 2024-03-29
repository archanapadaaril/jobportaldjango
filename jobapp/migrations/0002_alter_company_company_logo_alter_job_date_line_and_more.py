# Generated by Django 4.1.7 on 2023-04-24 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='Company', verbose_name='company_logo'),
        ),
        migrations.AlterField(
            model_name='job',
            name='Date_line',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='Date_line',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, upload_to='JobDetails', verbose_name='company_logo'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='published_on',
            field=models.CharField(max_length=20),
        ),
    ]
