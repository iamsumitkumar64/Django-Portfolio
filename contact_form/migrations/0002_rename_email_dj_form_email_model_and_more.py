# Generated by Django 5.1.2 on 2024-12-28 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dj_form',
            old_name='email',
            new_name='email_model',
        ),
        migrations.RenameField(
            model_name='dj_form',
            old_name='message',
            new_name='message_model',
        ),
        migrations.RenameField(
            model_name='dj_form',
            old_name='mobile',
            new_name='mobile_model',
        ),
        migrations.RenameField(
            model_name='dj_form',
            old_name='name',
            new_name='name_model',
        ),
    ]
