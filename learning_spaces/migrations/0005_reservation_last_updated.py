# Generated by Django 2.2.13 on 2020-08-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_spaces', '0004_auto_20200614_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]