# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chunks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chunk',
            name='description',
            field=models.CharField(help_text='Short Description', max_length=64, verbose_name='Description', blank=True),
        ),
    ]
