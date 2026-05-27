# Day 3 - Authentication, Personalization, and Persistent User State

## Lesson Goal

Build on Day 2 by introducing authenticated users and personalized settings.

By the end of Day 3, students will understand how to:
- log in to a web app
- fetch authenticated user and profile data through protected API calls
- open a dedicated user settings component from the main page
- show first/last name and allow editing
- store UI preferences in a backend profile model
- auto-save theme/font-size preferences from the main page
- reload persisted user state when the app starts

## Concepts Introduced

- Django built-in `User` model
- Django REST Framework token authentication
- authenticated API endpoints
- One-to-one profile model (`UserProfile`) for app-specific user settings
- protected read/update profile API
- controlled user updates (`first_name`, `last_name` only)
- React authenticated state (`token` in local storage)
- settings modal/panel pattern for clean UI separation
- optimistic UI + auto-save for simple preferences

## Backend Steps

## 1. Add authentication support

We use DRF Token Authentication because it is simple for a beginner workshop:
- user sends username/password to login endpoint
- backend returns a token
- frontend stores token and sends it in `Authorization: Token <token>` header

### Settings change

File: `backend/medisp_image_lab/settings.py`

- Added `rest_framework.authtoken` to `INSTALLED_APPS`
- Configured DRF default authentication class:
  - `rest_framework.authentication.TokenAuthentication`

## 2. Create `UserProfile` model

File: `backend/image_api/models.py`

Created `UserProfile` with `OneToOneField` to `User` and fields:
- `theme` (`light` / `dark`)
- `font_size` (`small` / `medium` / `large`)

Why this model exists:
- keep authentication data in Django `User`
- keep app preferences in a separate profile model

## 3. Add serializers

File: `backend/image_api/serializers.py`

- `CurrentUserSerializer` exposes:
  - `username`
  - `first_name`
  - `last_name`
  - `email`
  - `last_login`
- `CurrentUserUpdateSerializer` allows editing only:
  - `first_name`
  - `last_name`
- `UserProfileSerializer` exposes and updates:
  - `theme`
  - `font_size`

## 4. Add API endpoints

File: `backend/image_api/views.py`

Implemented endpoints:
- `POST /api/login/`
  - public endpoint
  - validates username/password
  - returns token
- `POST /api/logout/`
  - authenticated endpoint
  - deletes current token
- `GET /api/me/`
  - authenticated endpoint
  - returns current user fields
- `PATCH /api/me/`
  - authenticated endpoint
  - updates only `first_name` and `last_name` for `request.user`
- `GET /api/profile/`
  - authenticated endpoint
  - returns current user's profile
- `PATCH /api/profile/`
  - authenticated endpoint
  - updates current user's profile preferences

Security rules for Day 3:
- user can only access their own data (`request.user` only)
- frontend cannot edit `username`, `email`, or `last_login`

## 5. Register URL routes

File: `backend/image_api/urls.py`

Routes:
- `/api/login/`
- `/api/logout/`
- `/api/me/`
- `/api/profile/`
- `/api/process-image/`

## 6. Add migration

File: `backend/image_api/migrations/0001_initial.py`

This migration creates the `UserProfile` table.

## Frontend Steps

Files:
- `frontend/src/App.js`
- `frontend/src/App.css`

## 1. Add login/logout flow

- Login form for username/password
- On success:
  - store token in `localStorage` (`medispToken`)
- Logout button:
  - call `/api/logout/`
  - clear local token and session UI state

## 2. Maintain authenticated session

- On app startup:
  - read token from `localStorage`
  - call authenticated `GET /api/me/` and `GET /api/profile/`
- If token invalid:
  - clear token
  - return user to login screen

## 3. Keep main page focused

Main page contains:
- image upload
- grayscale processing button
- original + processed image previews
- compact personalization controls in top-right:
  - theme toggle icon
  - font-size toggle icon

Theme and font-size updates auto-save with `PATCH /api/profile/`.

## 4. Add top-right user settings button

- Added `User Settings` button near `Logout`
- Clicking opens a modal component (simple and easy for teaching)

## 5. User settings component behavior

Inside the modal:

User information section:
- Display (read-only):
  - `username`
  - `email`
  - `last_login`

Name editing section:
- If first/last name exists, display full name as text button
- Click that text to switch into edit mode
- Edit fields:
  - `first_name`
  - `last_name`
- Save with `PATCH /api/me/`

Profile preferences section (main page):
- `theme` and `font_size` are controlled from top-right icon toggles
- Changes are auto-saved to `/api/profile/`

## Commands Used

## Backend setup

```bash
cd backend
source ~/.venvs/medisp-image-lab/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Create a demo user

```bash
python manage.py createsuperuser
```

(You can also create normal users from Django admin.)

## Run backend

```bash
python manage.py runserver
```

## Frontend setup

```bash
cd frontend
npm install
npm start
```

## API Examples

## 1. Login

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"demo1234"}'
```

Response example:

```json
{
  "token": "a1b2c3d4..."
}
```

## 2. Get current user

```bash
curl http://127.0.0.1:8000/api/me/ \
  -H "Authorization: Token a1b2c3d4..."
```

Response example:

```json
{
  "username": "demo",
  "first_name": "Demo",
  "last_name": "User",
  "email": "demo@example.com",
  "last_login": "2026-05-09 10:30:12"
}
```

## 3. Update current user (safe fields only)

```bash
curl -X PATCH http://127.0.0.1:8000/api/me/ \
  -H "Authorization: Token a1b2c3d4..." \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Anna","last_name":"Smith"}'
```

## 4. Get profile

```bash
curl http://127.0.0.1:8000/api/profile/ \
  -H "Authorization: Token a1b2c3d4..."
```

Response example:

```json
{
  "theme": "light",
  "font_size": "medium"
}
```

## 5. Update profile preferences

```bash
curl -X PATCH http://127.0.0.1:8000/api/profile/ \
  -H "Authorization: Token a1b2c3d4..." \
  -H "Content-Type: application/json" \
  -d '{"theme":"dark","font_size":"large"}'
```

## 6. Logout

```bash
curl -X POST http://127.0.0.1:8000/api/logout/ \
  -H "Authorization: Token a1b2c3d4..."
```

## Testing Steps (Live Demo Checklist)

1. Start backend and frontend.
2. Create a test user in Django admin or via `createsuperuser`.
3. Open `http://localhost:3000`.
4. Confirm login form is visible.
5. Login with test user credentials.
6. Confirm main page focuses on image upload and grayscale workflow.
7. Use top-right theme icon toggle and confirm automatic visual update.
8. Use top-right font-size icon toggle and confirm automatic text-size update.
9. Refresh browser and confirm theme/font-size persisted.
10. Click `User Settings` in top-right area.
11. Confirm modal opens with username/email/last-login.
12. If a name exists, click displayed name to edit.
13. Save name and verify updated display.
14. Logout and confirm app returns to login screen.

## Educational Explanations for Students

- Authentication answers: "Who is the user?"
- Authorization answers: "What is this user allowed to access?"

In this lesson:
- `TokenAuthentication` identifies the user from a token.
- We never allow client-side user IDs for reads/updates.
- Backend always uses `request.user`, so each user only sees and updates their own data.

Why separate settings into a component:
- main workflow (image processing) stays clear and focused
- account fields are grouped in one place

Why keep theme/font controls on main page:
- quick personalization without opening modal
- instant feedback
- easy demo of auto-save behavior

Why split updates by endpoint:
- `/api/me/` updates only safe identity fields (`first_name`, `last_name`)
- `/api/profile/` updates app preferences (`theme`, `font_size`)
- prevents accidental edits of protected fields like `username` and `email`
