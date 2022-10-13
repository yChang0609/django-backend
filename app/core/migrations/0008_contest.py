# Generated by Django 4.0.8 on 2022-10-07 18:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='活動名稱')),
                ('date', models.CharField(blank=True, max_length=255, null=True, verbose_name='活動開始結束')),
                ('origanizer', models.CharField(blank=True, max_length=255, null=True, verbose_name='活動單位')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='活動連結')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='活動圖片')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='活動tags')),
            ],
            options={
                'verbose_name': '活動',
                'verbose_name_plural': 's',
            },
        ),
    ]
