# Generated by Django 3.2.9 on 2021-11-27 15:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Administrators',
            new_name='Administrator',
        ),
    ]
