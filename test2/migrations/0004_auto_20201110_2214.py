# Generated by Django 3.0.7 on 2020-11-10 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0003_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
