# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0003_comentario_replica'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='pergunta',
            field=models.ForeignKey(to='FAQ.Topico', null=True),
            preserve_default=True,
        ),
    ]
