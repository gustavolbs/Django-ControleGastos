# Generated by Django 2.1.2 on 2018-10-18 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0065_auto_20181018_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 14, 10, 5, 938868, tzinfo=utc)),
        ),
    ]
