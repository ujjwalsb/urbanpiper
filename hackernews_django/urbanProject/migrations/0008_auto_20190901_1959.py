# Generated by Django 2.2.4 on 2019-09-01 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urbanProject', '0007_auto_20190901_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hackernewsapi',
            old_name='auto_increment_id',
            new_name='serial_id',
        ),
    ]