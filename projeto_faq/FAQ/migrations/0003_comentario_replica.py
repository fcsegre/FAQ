# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0002_resposta_pergunta'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='replica',
            field=models.ForeignKey(to='FAQ.Resposta', null=True),
            preserve_default=True,
        ),
    ]
