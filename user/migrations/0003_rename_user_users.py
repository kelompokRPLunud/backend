# Generated by Django 4.1.4 on 2022-12-29 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_username_user_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]