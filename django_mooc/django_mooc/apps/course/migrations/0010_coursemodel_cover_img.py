# Generated by Django 3.0.1 on 2020-02-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20200208_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodel',
            name='cover_img',
            field=models.ImageField(default='default/course_cover.png', upload_to='course/cover/%Y/%m/%d', verbose_name='课程封面'),
        ),
    ]