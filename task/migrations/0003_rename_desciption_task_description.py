# Generated by Django 4.0.6 on 2022-07-15 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_user_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='desciption',
            new_name='description',
        ),
    ]
