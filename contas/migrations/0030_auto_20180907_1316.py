# Generated by Django 2.1 on 2018-09-07 16:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0029_auto_20180907_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 7, 16, 16, 8, 153889, tzinfo=utc)),
        ),
    ]
