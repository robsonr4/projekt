# Generated by Django 3.1.3 on 2021-01-02 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20210102_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_points',
            new_name='task_points_scored',
        ),
    ]