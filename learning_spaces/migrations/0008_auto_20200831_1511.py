# Generated by Django 2.2.1 on 2020-08-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_spaces', '0007_auto_20200831_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='beamer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='board',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='whiteboard',
            field=models.BooleanField(default=False),
        ),
    ]