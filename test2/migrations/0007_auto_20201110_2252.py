# Generated by Django 3.0.7 on 2020-11-10 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0006_activities_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Register_User'),
        ),
    ]