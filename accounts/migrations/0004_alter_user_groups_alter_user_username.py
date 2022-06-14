# Generated by Django 4.0.5 on 2022-06-14 03:03

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0003_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user', name='groups', field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to.'
                ' A user will get all permissions granted to'
                ' each of their groups.',
                related_name='user_set', related_query_name='user',
                to='auth.group', verbose_name='groups'),),
        migrations.AlterField(
            model_name='user', name='username', field=models.CharField(
                error_messages={
                    'unique':
                    'A user with that username already exists.'},
                help_text='Required. 150 characters or fewer.'
                'Letters, digits and @/./+/-/_ only.',
                max_length=150, unique=True,
                validators=[django.contrib.auth.validators.
                            UnicodeUsernameValidator()],
                verbose_name='username'),), ]