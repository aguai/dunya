# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 09:32
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='mbid',
            field=django_extensions.db.fields.UUIDField(max_length=36, blank=True, editable=False),
            preserve_default=False,
        ),
        migrations.RunSQL('alter table data_collection alter COLUMN mbid type uuid USING ("mbid"::uuid)'),
        migrations.AlterField(
            model_name='collection',
            name='mbid',
            field=models.UUIDField(db_index=True),
        ),
        migrations.RenameField(
            model_name='collection',
            old_name='mbid',
            new_name='collectionid'
        ),
    ]
