# Generated by Django 3.1.4 on 2021-01-01 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_subject_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject_ingredient',
            name='max_points',
            field=models.IntegerField(default=50),
        ),
    ]
