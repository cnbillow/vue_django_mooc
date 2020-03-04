from rest_framework import serializers

from course.models import *


class TeacherSerializer(serializers.ModelSerializer):
    """
        讲师
    """

    class Meta:
        model = Teacher
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    """
        课程标签
    """

    class Meta:
        model = Tag
        fields = ['name']


class CourseSerializer(serializers.ModelSerializer):
    """
        课程列表中的课程
    """
    tag = TagSerializer(read_only=True, many=True)
    teachers = TeacherSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        exclude = ['h5_desc', 'has_chapter', 'chapter']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True, many=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class FullCourseSerializer(CourseSerializer):
    """
        课程列表中的课程
    """
    tag = TagSerializer(read_only=True, many=True)
    teachers = TeacherSerializer(read_only=True, many=True)
    chapter = ChapterSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        exclude = []
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """
        轮播图左侧导航条的子类
    """

    class Meta:
        model = Category
        fields = '__all__'


class NavSerializer(serializers.ModelSerializer):
    """
        导航
    """
    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = BannerNav
        fields = '__all__'


class PlayRecordSerializer(serializers.ModelSerializer):
    """
        播放记录
    """
    title = serializers.CharField(source='lesson.title', read_only=True)
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    cover = serializers.SerializerMethodField()

    class Meta:
        model = PlayRecord
        exclude = ['id']

    def get_cover(self, obj):
        course = obj.lesson.lesson_chapter.all()[0].chapter_course.all()[0]
        course_serializer = CourseSerializer(course, context={'request': self.context['request']})

        return course_serializer.data['cover_img']
