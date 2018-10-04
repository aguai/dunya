# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-29 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20180827_1752'),
        ('jingju', '0002_auto_20180828_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordingInstrumentalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='performer',
            name='roletype',
        ),
        migrations.RemoveField(
            model_name='recordingartist',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='recordingartist',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='recordingartist',
            name='recording',
        ),
        migrations.RemoveField(
            model_name='recording',
            name='performer',
        ),
        migrations.AddField(
            model_name='artist',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jingju', to='jingju.Instrument'),
        ),
        migrations.AddField(
            model_name='artist',
            name='role_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jingju.RoleType'),
        ),
        migrations.AddField(
            model_name='recording',
            name='performers',
            field=models.ManyToManyField(related_name='performer', through='jingju.RecordingPerformer', to='jingju.Artist'),
        ),
        migrations.AddField(
            model_name='release',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Collection'),
        ),
        migrations.AddField(
            model_name='roletype',
            name='uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='play',
            name='uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recording',
            name='instrumentalists',
            field=models.ManyToManyField(related_name='instrumentalist', through='jingju.RecordingInstrumentalist', to='jingju.Artist'),
        ),
        migrations.AlterField(
            model_name='recordingperformer',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jingju.Artist'),
        ),
        migrations.AlterField(
            model_name='release',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jingju.Artist'),
        ),
        migrations.AlterField(
            model_name='score',
            name='uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Performer',
        ),
        migrations.DeleteModel(
            name='RecordingArtist',
        ),
        migrations.AddField(
            model_name='recordinginstrumentalist',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jingju.Artist'),
        ),
        migrations.AddField(
            model_name='recordinginstrumentalist',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jingju.Instrument'),
        ),
        migrations.AddField(
            model_name='recordinginstrumentalist',
            name='recording',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jingju.Recording'),
        ),
    ]