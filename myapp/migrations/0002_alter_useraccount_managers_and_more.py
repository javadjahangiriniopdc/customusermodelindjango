# Generated by Django 4.0.4 on 2022-05-07 08:46

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='useraccount',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
