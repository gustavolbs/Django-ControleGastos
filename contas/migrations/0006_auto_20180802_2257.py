# Generated by Django 2.1 on 2018-08-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_auto_20180802_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
