# Generated by Django 3.0.1 on 2020-02-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200208_1921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapterlessonmodel',
            options={'ordering': ['index'], 'verbose_name': '课程章节课时', 'verbose_name_plural': '课程章节课时'},
        ),
        migrations.AlterField(
            model_name='coursemodel',
            name='h5_desc',
            field=models.TextField(blank=True, null=True, verbose_name='html格式描述内容'),
        ),
    ]