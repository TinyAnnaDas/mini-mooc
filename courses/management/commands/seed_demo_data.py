from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson, Enrollment


class Command(BaseCommand):
    help = "Create demo users, a sample course, lessons, and an enrollment for quick review."

    def handle(self, *args, **options):
        User = get_user_model()

        # Demo superuser
        admin_username = "admin"
        admin_password = "admin123"
        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(
                username=admin_username,
                email="admin@example.com",
                password=admin_password,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created superuser {admin_username} / {admin_password}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Superuser '{admin_username}' already exists.")
            )

        # Demo student user
        student_username = "student"
        student_password = "student123"
        student, created = User.objects.get_or_create(
            username=student_username,
            defaults={"email": "student@example.com"},
        )
        if created:
            student.set_password(student_password)
            student.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created student user {student_username} / {student_password}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"User '{student_username}' already exists.")
            )

        # Sample course and lessons
        course, created = Course.objects.get_or_create(
            title="Django Basics: Build a Mini MOOC",
            defaults={
                "short_description": "Learn how to build a simple online course platform with Django.",
                "long_description": (
                    "In this mini-course, you will build a small MOOC-style application using Django. "
                    "You will learn how to model courses and lessons, handle user enrollments, "
                    "and track basic lesson progress."
                ),
            },
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Created demo course: {course.title}")
            )

        if not course.lessons.exists():
            lesson_specs = [
                (
                    "Setting Up the Django Project",
                    "Create the Django project and configure settings, then run the development server.",
                ),
                (
                    "Modeling Courses and Lessons",
                    "Define Course, Lesson, Enrollment, and LessonProgress models and run migrations.",
                ),
                (
                    "Enrollments and Lesson Progress",
                    "Allow users to enroll in courses and record which lessons they have viewed.",
                ),
            ]
            for title, content in lesson_specs:
                Lesson.objects.create(course=course, title=title, content=content)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created {len(lesson_specs)} demo lessons for {course.title}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"Course '{course.title}' already has lessons; skipping lesson creation."
                )
            )

        # Enroll the student in the course
        Enrollment.objects.get_or_create(user=student, course=course)
        self.stdout.write(
            self.style.SUCCESS(
                f"Ensured enrollment: {student_username} is enrolled in '{course.title}'."
            )
        )

        # Second sample course
        course2, created2 = Course.objects.get_or_create(
            title="Introduction to Python Programming",
            defaults={
                "short_description": "Learn the fundamentals of Python programming from scratch.",
                "long_description": (
                    "This course introduces you to Python programming basics. "
                    "You'll learn about variables, data types, control flow, functions, "
                    "and basic data structures. Perfect for beginners who want to start their programming journey."
                ),
            },
        )
        if created2:
            self.stdout.write(
                self.style.SUCCESS(f"Created demo course: {course2.title}")
            )

        if not course2.lessons.exists():
            lesson_specs2 = [
                (
                    "Getting Started with Python",
                    "Install Python, set up your development environment, and write your first Python program.",
                ),
                (
                    "Variables and Data Types",
                    "Learn about integers, floats, strings, booleans, and how to work with variables.",
                ),
                (
                    "Control Flow: Conditionals and Loops",
                    "Master if/else statements, for loops, and while loops to control program execution.",
                ),
                (
                    "Functions and Modules",
                    "Create reusable functions and organize your code using Python modules.",
                ),
            ]
            for title, content in lesson_specs2:
                Lesson.objects.create(course=course2, title=title, content=content)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created {len(lesson_specs2)} demo lessons for {course2.title}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"Course '{course2.title}' already has lessons; skipping lesson creation."
                )
            )
