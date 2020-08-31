# Generated by Django 2.2.1 on 2020-08-31 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_spaces', '0005_reservation_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='ressources',
            field=models.CharField(choices=[('BE', 'Beamer'), ('WB', 'Whiteboard'), ('BO', 'Normale Tafel')], default=None, max_length=2),
        ),
    ]
