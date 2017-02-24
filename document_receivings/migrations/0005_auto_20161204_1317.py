# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('document_receivings', '0004_auto_20161204_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='document',
            name='modified_on',
        ),
        migrations.RemoveField(
            model_name='verification',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='verification',
            name='modified_on',
        ),
        migrations.AddField(
            model_name='document',
            name='verified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='documents_verified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='verified_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='verification',
            name='verified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='document_verifications_verified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='verification',
            name='verified_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='documents_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='verification',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='document_verifications_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
