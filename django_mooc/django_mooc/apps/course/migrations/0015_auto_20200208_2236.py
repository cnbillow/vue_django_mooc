# Generated by Django 3.0.1 on 2020-02-08 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20200208_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecategorymodel',
            old_name='index',
            new_name='level',
        ),
    ]