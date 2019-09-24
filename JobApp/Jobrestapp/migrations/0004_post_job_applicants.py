# Generated by Django 2.2.5 on 2019-09-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobrestapp', '0003_post_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_job',
            name='applicants',
            field=models.ManyToManyField(related_name='applicants', to='Jobrestapp.Applicant'),
        ),
    ]
