# Generated by Django 3.0.1 on 2020-02-08 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_coursemodel_teacher'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teachermodel',
            unique_together={('name', 'nick_name', 'desc')},
        ),
    ]