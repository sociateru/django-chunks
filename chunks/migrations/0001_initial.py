# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(help_text='A unique name for this chunk of content', unique=True, max_length=255, verbose_name='Key')),
                ('content', models.TextField(verbose_name='Content', blank=True)),
            ],
            options={
                'verbose_name': 'chunk',
                'verbose_name_plural': 'chunks',
            },
        ),
    ]
