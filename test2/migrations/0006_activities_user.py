# Generated by Django 3.0.7 on 2020-11-10 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0005_remove_activities_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='test2.Register_User'),
        ),
    ]
