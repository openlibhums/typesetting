# Generated by Django 3.2.20 on 2024-07-08 16:27

import core.model_utils
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('typesetting', '0016_store_blank_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleyproofing',
            name='notes',
            field=core.model_utils.JanewayBleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='galleyproofing',
            name='task',
            field=core.model_utils.JanewayBleachField(help_text='Add any additional information or instructions for the proofreader here.', verbose_name='Proofing Task'),
        ),
        migrations.AlterField(
            model_name='typesettingassignment',
            name='task',
            field=core.model_utils.JanewayBleachField(blank=True, help_text='Please let the typesetter know what you want them to create and if there are any special circumstances. They will have access to the article’s metadata.', verbose_name='Typesetting Task'),
        ),
        migrations.AlterField(
            model_name='typesettingassignment',
            name='typesetter_note',
            field=core.model_utils.JanewayBleachField(blank=True, verbose_name='Note to Editor'),
        ),
    ]
