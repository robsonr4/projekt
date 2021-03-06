# Generated by Django 3.1.3 on 2021-01-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_auto_20210114_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='max_points',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_points_max',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_points_scored',
            field=models.FloatField(),
        ),
    ]
