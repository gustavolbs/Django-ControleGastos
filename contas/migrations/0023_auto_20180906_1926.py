# Generated by Django 2.1 on 2018-09-06 22:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0022_auto_20180906_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 22, 26, 25, 813763, tzinfo=utc)),
        ),
    ]