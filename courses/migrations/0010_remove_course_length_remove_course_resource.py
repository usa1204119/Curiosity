# Generated by Django 4.1.12 on 2024-03-25 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_payment_user_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='length',
        ),
        migrations.RemoveField(
            model_name='course',
            name='resource',
        ),
    ]
