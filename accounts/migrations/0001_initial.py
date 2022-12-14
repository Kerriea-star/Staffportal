# Generated by Django 4.0.5 on 2022-07-29 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('full_name', models.CharField(max_length=200, verbose_name='full name')),
                ('username', models.CharField(max_length=70, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=250, unique=True, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='phone')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('role', models.CharField(choices=[('administrator', 'administrator'), ('worker', 'worker')], max_length=50, verbose_name='role')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timeatamp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='profile_pictures', verbose_name='profile picture')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('first_name', models.CharField(max_length=200, verbose_name='first name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last name')),
                ('company', models.CharField(blank=True, max_length=250, null=True, verbose_name='company')),
                ('department', models.CharField(blank=True, max_length=250, null=True, verbose_name='department')),
                ('year', models.DateTimeField(auto_now_add=True, verbose_name='year')),
                ('county', models.CharField(blank=True, max_length=100, null=True, verbose_name='county')),
                ('town', models.CharField(blank=True, max_length=100, null=True, verbose_name='town')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='address')),
                ('postal_code', models.CharField(blank=True, max_length=70, null=True, verbose_name='postal code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='profile_pictures', verbose_name='profile picture')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=70, verbose_name='last name')),
                ('county', models.CharField(blank=True, max_length=80, null=True, verbose_name='county')),
                ('town', models.CharField(blank=True, max_length=80, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=90, verbose_name='estate')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'abstract': False,
            },
        ),
    ]
