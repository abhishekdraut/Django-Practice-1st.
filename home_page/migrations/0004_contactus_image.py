# Generated by Django 3.2.5 on 2021-09-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_auto_20210818_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='image',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
