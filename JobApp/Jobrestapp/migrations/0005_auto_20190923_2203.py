# Generated by Django 2.2.5 on 2019-09-23 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobrestapp', '0004_post_job_applicants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_job',
            old_name='job_title',
            new_name='Job_title',
        ),
    ]
