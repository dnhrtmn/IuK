# Generated by Django 2.2.13 on 2020-06-06 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(default='', max_length=25)),
                ('last_name', models.CharField(default='', max_length=25)),
                ('postalcode', models.IntegerField(blank=True, default=0)),
                ('city', models.CharField(default='', max_length=25)),
                ('adress', models.CharField(default='', max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=100)),
                ('location', models.TextField()),
                ('size', models.TextField(max_length=3)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('start_time', models.DateField(default=django.utils.timezone.now)),
                ('room', models.CharField(blank=True, default='', max_length=5, verbose_name='Room')),
                ('block', models.CharField(blank=True, default='', max_length=1)),
                ('identifier', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
