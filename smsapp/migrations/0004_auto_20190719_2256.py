# Generated by Django 2.2.3 on 2019-07-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0003_auto_20190717_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(max_length=200, verbose_name='Текст'),
        ),
    ]
