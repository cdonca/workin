# Generated by Django 2.0.9 on 2019-06-15 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import userena.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserenaSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_active', models.DateTimeField(blank=True, help_text='The last date that the user was active.', null=True, verbose_name='last active')),
                ('activation_key', models.CharField(blank=True, max_length=40, verbose_name='activation key')),
                ('activation_notification_send', models.BooleanField(default=False, help_text='Designates whether this user has already got a notification about activating their account.', verbose_name='notification send')),
                ('email_unconfirmed', models.EmailField(blank=True, help_text='Temporary email address when the user requests an email change.', max_length=254, verbose_name='unconfirmed email address')),
                ('email_confirmation_key', models.CharField(blank=True, max_length=40, verbose_name='unconfirmed email verification key')),
                ('email_confirmation_key_created', models.DateTimeField(blank=True, null=True, verbose_name='creation date of email confirmation key')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userena_signup', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'userena registration',
                'verbose_name_plural': 'userena registrations',
            },
            managers=[
                ('objects', userena.managers.UserenaManager()),
            ],
        ),
    ]
