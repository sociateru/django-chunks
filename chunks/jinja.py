# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from django import template
from django.apps import apps
from django.core.cache import cache

import jinja2


register = template.Library()

Chunk = apps.get_model('chunks', 'chunk')
CACHE_PREFIX = 'chunk_content_'


def chunk_content(key_name, cache_time=0):
    cache_key = CACHE_PREFIX + key_name
    cache_time = int(cache_time)

    content = cache.get(cache_key)
    if content is None:
        try:
            c = Chunk.objects.get(key=key_name)
        except Chunk.DoesNotExist:
            content = ''
        else:
            content = c.content
        cache.set(cache_key, content, cache_time)

    return jinja2.Markup(content)
