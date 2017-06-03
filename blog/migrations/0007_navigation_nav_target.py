# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 02:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_navigation_nav_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='nav_target',
            field=models.CharField(choices=[('_blank', 'BLANK'), ('_parent', 'PARENT'), ('_self', 'SELF'), ('_top', 'TOP')], default='_self', max_length=10),
            preserve_default=False,
        ),
    ]
