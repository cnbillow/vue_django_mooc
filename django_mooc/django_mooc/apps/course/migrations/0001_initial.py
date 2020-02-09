# Generated by Django 3.0.1 on 2020-02-09 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('sub_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='副标题')),
                ('ordering', models.PositiveSmallIntegerField(default=1, verbose_name='轮播图序号')),
                ('url', models.URLField(default='/', verbose_name='跳转链接')),
                ('img', models.ImageField(default='default/banner.png', upload_to='banners/%Y/%m/%d', verbose_name='图片（建议尺寸960*425）')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
                'db_table': 'geng_banner',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='分类名')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='分类别名')),
                ('level', models.PositiveSmallIntegerField(choices=[(1, '一级分类'), (2, '二级分类'), (3, '三级分类')], default=1, verbose_name='分类级别')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Category', verbose_name='上级分类')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'geng_course_category',
                'unique_together': {('title', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='最新章节', max_length=32, unique=True, verbose_name='章节名称')),
                ('joined_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '课程章节',
                'verbose_name_plural': '课程章节',
                'db_table': 'geng_chapter',
                'ordering': ['pk'],
                'get_latest_by': 'index',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='最新课时', max_length=32, verbose_name='课时标题')),
                ('joined_item', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '课程章节课时',
                'verbose_name_plural': '课程章节课时',
                'db_table': 'geng_lesson',
                'ordering': ['pk'],
                'get_latest_by': 'index',
            },
        ),
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机构名称')),
            ],
            options={
                'verbose_name': '机构',
                'verbose_name_plural': '机构',
                'db_table': 'geng_org',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '课程标签',
                'verbose_name_plural': '课程标签',
                'db_table': 'geng_tag',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='讲师名称')),
                ('nick_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='讲师昵称')),
                ('avatar', models.ImageField(default='default/avatar.png', upload_to='avatars/%Y/%m/%d', verbose_name='头像')),
                ('desc', models.TextField(verbose_name='讲师介绍')),
                ('org', models.ManyToManyField(to='course.Org', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '讲师',
                'verbose_name_plural': '讲师',
                'db_table': 'geng_teacher',
                'unique_together': {('name', 'nick_name', 'desc')},
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='导航名称(5~7个)')),
                ('ordering', models.PositiveIntegerField(default=1, verbose_name='显示顺序')),
                ('category', models.ManyToManyField(to='course.Category', verbose_name='课程分类')),
            ],
            options={
                'verbose_name': '导航',
                'verbose_name_plural': '导航',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='标题')),
                ('cover_img', models.ImageField(default='default/course_cover.png', upload_to='course/cover/%Y/%m/%d', verbose_name='课程封面')),
                ('sub_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='副标题')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('h5_desc', models.TextField(blank=True, null=True, verbose_name='h5格式描述')),
                ('url', models.TextField(blank=True, null=True, verbose_name='课程链接')),
                ('video_url', models.TextField(blank=True, null=True, verbose_name='视频链接(课程只有一个视频时有效)')),
                ('price', models.CharField(default='免费', max_length=11, verbose_name='价格')),
                ('has_activity_price', models.BooleanField(default=False, verbose_name='是否有活动价格')),
                ('activity_price', models.CharField(default='免费', max_length=11, verbose_name='活动价格')),
                ('has_chapter', models.BooleanField(default=False, verbose_name='是否具有章节')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.Category', verbose_name='课程类别')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Chapter', verbose_name='课程的所有章节')),
                ('tag', models.ManyToManyField(to='course.Tag', verbose_name='课程标签')),
                ('teachers', models.ManyToManyField(to='course.Teacher', verbose_name='讲师')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'db_table': 'geng_course',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.Lesson', verbose_name='课时'),
        ),
    ]
