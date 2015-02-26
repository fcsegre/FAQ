# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resposta',
            name='pergunta',
            field=models.ForeignKey(to='FAQ.Topico', null=True),
            preserve_default=True,
        ),
    ]
