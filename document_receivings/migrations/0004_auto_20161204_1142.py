# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document_receivings', '0003_auto_20161204_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verification',
            options={'permissions': (('can_verify_document', 'Can Verify Document'),)},
        ),
    ]