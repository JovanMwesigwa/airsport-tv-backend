# Generated by Django 4.0.5 on 2022-06-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportevents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportevent',
            name='main',
            field=models.BooleanField(default=False),
        ),
    ]