from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SignUpForm
from .models import Course, Enrollment, Lesson, LessonProgress


def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()

    user_is_enrolled = False
    viewed_lesson_ids = set()
    if request.user.is_authenticated:
        user_is_enrolled = Enrollment.objects.filter(
            user=request.user,
            course=course,
        ).exists()
        viewed_lesson_ids = set(
            LessonProgress.objects.filter(
                user=request.user,
                lesson__course=course,
            ).values_list("lesson_id", flat=True)
        )

    context = {
        "course": course,
        "lessons": lessons,
        "user_is_enrolled": user_is_enrolled,
        "viewed_lesson_ids": viewed_lesson_ids,
    }
    return render(request, "courses/course_detail.html", context)


@login_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect("courses:course_detail", pk=course.pk)


@login_required
def my_courses(request):
    enrollments = (
        Enrollment.objects.select_related("course")
        .filter(user=request.user)
        .order_by("-enrolled_at")
    )
    courses = [enrollment.course for enrollment in enrollments]
    return render(request, "courses/my_courses.html", {"courses": courses})


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    LessonProgress.objects.update_or_create(
        user=request.user,
        lesson=lesson,
        defaults={},
    )

    return render(request, "courses/lesson_detail.html", {"lesson": lesson})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("courses:course_list")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


