# Generated by Django 4.1 on 2022-08-24 12:13

import app_news.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(validators=[app_news.validators.validate_gmt], verbose_name='phone number')),
                ('GMT', models.IntegerField(validators=[app_news.validators.validate_gmt], verbose_name='GMT')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('text', models.TextField(max_length=10000, verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='name')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='app_news.client', verbose_name='client')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='app_news.newsletter', verbose_name='newsletter')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='app_news.status', verbose_name='status')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='app_news.phonecode', verbose_name='country code'),
        ),
        migrations.AddField(
            model_name='client',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='app_news.tag', verbose_name='tag'),
        ),
    ]