# Generated by Django 2.2.5 on 2019-09-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_applicant_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Email',
            field=models.EmailField(max_length=250),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='FirstName',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='LastName',
            field=models.CharField(max_length=250),
        ),
    ]
