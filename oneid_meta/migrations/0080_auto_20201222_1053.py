# Generated by Django 2.2.10 on 2020-12-22 02:53

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0079_auto_20200803_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='data',
            field=jsonfield.fields.JSONField(default=dict, verbose_name='信息内容'),
        ),
    ]