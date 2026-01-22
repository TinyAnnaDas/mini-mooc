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

### Quick Start (Using Scripts)

The easiest way to run the application:

```bash
# Run the application
./scripts/run.sh

# Or deploy (production-like)
./scripts/deploy.sh

# Stop the application
./scripts/stop.sh
```

### Manual Docker Commands

```bash
cd /Users/tinyannadas/the_tiny_developer/mini-mooc
docker compose build
docker compose up
```

The app will be available at `http://127.0.0.1:8000/`.

The container command automatically runs database migrations before starting the Django development server.

### Docker Scripts

- **`scripts/run.sh`**: Start the application for local development (with live logs)
- **`scripts/deploy.sh`**: Deploy the application (runs migrations, checks health)
- **`scripts/stop.sh`**: Stop all running containers

### Docker Compose Commands

```bash
# Build and start
docker compose up -d

# View logs
docker compose logs -f

# Stop containers
docker compose down

# Restart containers
docker compose restart

# Access container shell
docker compose exec web bash

# Run management commands
docker compose exec web python manage.py migrate
docker compose exec web python manage.py seed_demo_data
docker compose exec web python manage.py createsuperuser
```

## CI/CD with GitHub Actions

The project includes a GitHub Actions workflow (`.github/workflows/docker-build.yml`) that:

- Builds the Docker image on push/PR to `main` or `develop` branches
- Tests the Docker image by running it and checking health
- Tests Docker Compose setup

The workflow runs automatically on:
- Pushes to `main` or `develop` branches
- Pull requests targeting `main` or `develop` branches

View workflow runs in the **Actions** tab of your GitHub repository.

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

