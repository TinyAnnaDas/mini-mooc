from django.contrib import admin

from .models import Course, Lesson, Enrollment, LessonProgress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "created_at")
    search_fields = ("title", "short_description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "created_at")
    list_filter = ("course",)
    search_fields = ("title", "course__title")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "enrolled_at")
    list_filter = ("course", "user")
    search_fields = ("user__username", "course__title")


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "viewed_at")
    list_filter = ("lesson__course", "user")
    search_fields = ("user__username", "lesson__title", "lesson__course__title")
