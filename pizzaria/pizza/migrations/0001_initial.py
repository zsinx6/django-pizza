# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flavor', models.CharField(max_length=128)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ingredients', models.TextField()),
            ],
        ),
    ]
