# Generated by Django 3.2.5 on 2021-08-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_contactus_suggestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='address',
        ),
        migrations.AlterField(
            model_name='contactus',
            name='suggestions',
            field=models.CharField(max_length=500),
        ),
    ]
