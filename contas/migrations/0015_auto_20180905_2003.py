# Generated by Django 2.1 on 2018-09-05 23:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0014_auto_20180905_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 5, 23, 3, 28, 833655, tzinfo=utc)),
        ),
    ]
