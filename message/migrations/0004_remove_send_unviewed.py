# Generated by Django 4.2.1 on 2023-05-24 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_message_unviewed_send_unviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send',
            name='unviewed',
        ),
    ]
