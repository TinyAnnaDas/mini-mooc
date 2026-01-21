from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("courses/<int:pk>/", views.course_detail, name="course_detail"),
    path("courses/<int:pk>/enroll/", views.enroll_in_course, name="enroll_in_course"),
    path("my-courses/", views.my_courses, name="my_courses"),
    path("lessons/<int:pk>/", views.lesson_detail, name="lesson_detail"),
    path("signup/", views.signup, name="signup"),
]

