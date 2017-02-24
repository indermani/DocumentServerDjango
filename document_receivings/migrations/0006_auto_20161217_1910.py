# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document_receivings', '0005_auto_20161204_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifications', to='document_receivings.Document'),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together=set([('ref_no', 'doctype')]),
        ),
    ]
