## Mini MOOC – Simple Course Catalog

This is a very small MOOC-style course catalog built with Django. It lets users:

- Sign up and log in
- See a list of courses
- View course details and lesson lists
- Enroll in a course
- View lesson content
- Track which lessons a user has already visited

The project uses **Django** with **SQLite** for storage, and includes a basic **Docker** setup.

## Quickstart (local)

```bash
git clone <this-repo-url>
cd mini-mooc
python -m venv .venv
source .venv/bin/activate
pip install "django>=6.0.1"
python manage.py migrate
python manage.py seed_demo_data
python manage.py runserver
```

Then:

- Go to `http://127.0.0.1:8000/`
- Log in as:
  - admin user: `admin` / `admin123` (superuser, can use `/admin/`)
  - student user: `student` / `student123` (enrolled in the demo course)

## Local development (without Docker)

### Prerequisites

- Python 3.13
- `pip`

### Setup

```bash
cd /Users/tinyannadas/the_tiny_developer/mini-mooc
python -m venv .venv
source .venv/bin/activate
pip install "django>=6.0.1"
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in the browser.

### Admin

If you didn't run `python manage.py seed_demo_data` and want to create your own admin user:

```bash
python manage.py createsuperuser
```

Log in at `http://127.0.0.1:8000/admin/` and create:

- Courses
- Lessons under each course

## Running with Docker

### Build and run

```bash
cd /Users/tinyannadas/the_tiny_developer/mini-mooc
docker compose build
docker compose up
```

The app will be available at `http://127.0.0.1:8000/`.

The container command automatically runs database migrations before starting the Django development server.

## Key concepts

- **Course**: title, short description, long description, created timestamp.
- **Lesson**: belongs to a course, has title, content, and created timestamp.
- **Enrollment**: links a user to a course; one enrollment per user+course.
- **LessonProgress**: records that a given user has visited a given lesson.

## Main user flows

- Anonymous users can browse all courses and see course details, but must **log in to enroll**.
- Logged-in users can:
  - Enroll in a course from the course detail page.
  - See their enrolled courses under **My Courses**.
  - Open lessons; visiting a lesson records progress.
  - See which lessons they have already visited, marked as **(seen)** on the course detail page.

