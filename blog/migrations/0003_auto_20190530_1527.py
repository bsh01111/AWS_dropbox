# Generated by Django 2.0.13 on 2019-05-30 06:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_file_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]