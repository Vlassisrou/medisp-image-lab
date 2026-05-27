# Day 4 - Backend Testing and Docker Basics

## Learning goals

By the end of Day 4, students should be able to:

- explain what backend testing is
- run Django API tests with `manage.py test`
- understand what `APITestCase` gives us in DRF
- use coverage to see tested vs untested code
- run this full project with Docker Compose

## What is testing?

Testing is writing small checks that verify our code behaves as expected.

In backend APIs, tests help us confirm:

- login works correctly
- protected endpoints are actually protected
- user updates save the right fields
- API responses stay stable as the project grows

This helps us change code safely without breaking old features.

## Why backend testing matters

Frontend bugs are visible quickly. Backend bugs can be hidden until real users hit them.

Backend tests give confidence for:

- authentication and permissions
- data correctness
- regression protection ("it used to work")

## DRF testing with `APITestCase`

`APITestCase` is a Django REST Framework test class that gives us:

- an isolated test database per test run
- an API-friendly test client
- easy JSON requests and response assertions

In this project we also use:

- `APIClient` for token-auth request flows
- `force_authenticate` to quickly test protected endpoints

## What we test in Day 4

- login success and failure
- unauthorized access to `/api/me/` and `/api/profile/`
- authenticated reads from `/api/me/` and `/api/profile/`
- updating `first_name` and `last_name`
- ensuring read-only fields are not changed by `/api/me/`
- health check response from `/api/health/`

## Run backend tests

From the `backend/` folder:

```bash
python manage.py test
```

Coverage:

```bash
coverage run manage.py test
coverage report
```

## Health check endpoint

A simple endpoint is available for quick API checks:

- `GET /api/health/`

Expected JSON:

```json
{
  "status": "ok"
}
```

## What is Docker?

Docker packages an app and its dependencies into a container.

This means all students can run the same environment, even on different machines.

## Why Docker helps developers

- fewer "works on my machine" issues
- faster onboarding
- reproducible local setup

## Run this project with Docker Compose

From the project root:

```bash
docker compose up --build
```

Services:

- `backend` on port `8000`
- `frontend` on port `3000`

Stop containers:

```bash
docker compose down
```

## Useful debugging commands

```bash
docker compose logs backend
docker compose logs frontend
```

For local non-Docker development, tests still run the same way:

```bash
cd backend
python manage.py test
coverage run manage.py test
coverage report
```

## Homework (research only)

Do not implement these yet. Research the concepts:

- file upload
- media storage
- long-running tasks
- Celery
- Redis
- polling from frontend

Think about where these could fit in future versions of this app.

## Assumptions used in Day 4

- SQLite remains the database for this lesson.
- We keep Django and React in development mode for clarity.
- Docker setup is intentionally minimal for teaching.
