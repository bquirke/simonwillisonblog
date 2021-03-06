# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_agent', models.CharField(db_index=True, max_length=128)),
            ],
        ),
        migrations.AlterIndexTogether(
            name='subscribercount',
            index_together=set([('path', 'user_agent', 'count', 'created')]),
        ),
    ]
