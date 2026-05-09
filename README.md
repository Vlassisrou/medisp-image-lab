# medisp-image-lab

Day 3 training app: a beginner-friendly Django + React project that combines image processing with authentication and personalized user settings.

## What this app does

- Login with username/password
- Keep authenticated state using DRF token auth
- Open **User Settings** from the top-right area
- View user info (`username`, `email`, `last_login`)
- Edit `first_name` / `last_name`
- Toggle theme and font size from the main page (auto-saved)
- Upload an image and convert it to grayscale via backend API
- Display original and processed images side-by-side

## Tech stack

- Backend: Django, Django REST Framework, DRF Token Auth, Pillow
- Frontend: React (CRA), local CSS styling (no UI library)
- Database: SQLite (default)

## Project structure

- `backend/`: Django + DRF API
- `frontend/`: React app
- `Day_3.md`: detailed lesson notes for the training session

## API endpoints

- `POST /api/login/` -> returns auth token
- `POST /api/logout/` -> invalidates current token
- `GET /api/me/` -> current authenticated user
- `PATCH /api/me/` -> updates only `first_name` and `last_name`
- `GET /api/profile/` -> current user's profile preferences
- `PATCH /api/profile/` -> updates `theme` and `font_size`
- `POST /api/process-image/` -> grayscale conversion

Example process-image response:

```json
{
  "image": "<base64_string>"
}
```

## One-time setup

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### Frontend

In a second terminal:

```bash
cd frontend
npm install
```

## Run the app

### 1) Start backend

```bash
cd backend
source .venv/bin/activate
python manage.py runserver
```

### 2) Start frontend

In a second terminal:

```bash
cd frontend
npm start
```

## Browser flow

- Frontend: `http://localhost:3000`
- API uses CRA proxy to backend (`http://127.0.0.1:8000`)

### Expected Day 3 flow

1. Login with your user.
2. Use top-right icon toggles to change theme/font size (auto-save).
3. Open **User Settings**.
4. If a name exists, click it to edit first/last name.
5. Upload image and click **Process Image**.
6. Confirm grayscale output appears in the processed panel.

## Notes

- User updates are scoped to `request.user` for safety.
- `username`, `email`, and `last_login` are read-only from frontend.
- No CORS setup is needed for local demo because CRA proxy is configured.
