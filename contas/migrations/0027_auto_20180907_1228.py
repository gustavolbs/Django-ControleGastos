# Generated by Django 2.1 on 2018-09-07 15:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0026_auto_20180907_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 7, 15, 28, 4, 102858, tzinfo=utc)),
        ),
    ]
