# Generated by Django 4.0.3 on 2022-05-02 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_signup_master_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup_master',
            name='otp',
        ),
    ]