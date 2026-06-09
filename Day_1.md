# Day 1 – Environment Setup & First Run 🚀

Welcome to **Medisp Image Lab**.  
Today, we will go from **zero → running the backend and frontend applications**.

---

## 🎯 Goal of Day 1 my fist day

By the end of this session, you should be able to:

- Set up development tools and the environment if you want
- Clone a repository  
- Set up a Python environment  
- Run a Django backend  
- Run a React frontend  
- Make a small change and see it reflected  

---

## Using Visual Studio Code

Visual Studio Code is a lightweight and powerful code editor widely used for web development, supporting Python, JavaScript, and many modern technologies.

---

## Install Visual Studio Code come on boy you can do it

You can install Visual Studio Code directly from the Ubuntu Software application by searching for:

**Visual Studio Code**

---

## Terminal installation (recommended)

You can install Visual Studio Code using the terminal:

```bash
sudo snap install code --classic
```

---

## Verify installation

After installation, open a terminal and run:

```bash
code --version
```

If installed correctly, this will return the installed version.

---

## Recommended extensions

Once you open Visual Studio Code, install the following extensions:

* Python (by Microsoft)
* ESLint (optional)
* Prettier (optional)

To install extensions:

1. Open VS Code
2. Go to the Extensions tab (left sidebar)
3. Search and install the extensions listed above

---

## Notes

* Visual Studio Code will be used during the workshop for both backend (Python/Django) and frontend (React) development.
* No prior experience with VS Code is required.
* We will guide you through the necessary features during the sessions.

---

## 1. Clone the Repository

Git is a Version Control System (VCS) used to track changes in code and manage project history. It also facilitates cooperative software development.

---
## Install Git

```bash
sudo apt update
sudo apt install git -y
```

---

## Verify installation

```bash
git --version
```

---

## Configure Git (required)

Git needs your identity for commits:

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

---

## Clone the repository

Navigate to the folder where you want to store the project and run:

```bash
git clone https://github.com/gxenogiannopoulos/medisp-image-lab.git
cd medisp-image-lab
```

Switch to the Day 1 branch:

```bash
git checkout day-1
```

---

## Open the project in VS Code

```bash
code .
```

---

## Basic Git workflow

Check current status:

```bash
git status
```

Stage changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "your message"
```

---

## Project Structure

You should see something like:

```
medisp-image-lab/
│
├── backend/
├── frontend/
└── README.md
```

---

## 2. Backend Setup (Django)

Navigate to the backend:

```bash
cd ~/VsProjects/medisp-image-lab/backend
```

### Create a virtual environment

```bash
python3 --version
python3 -m venv ~/.venvs/medisp-image-lab
```

Activate it:

```bash
source ~/.venvs/medisp-image-lab/bin/activate
```

### Install Django

```bash
pip install --upgrade pip
pip install django djangorestframework
```

### Initialize project (if not already initialized)

```bash
django-admin startproject medisp_image_lab .
python manage.py startapp image_processing
```

Open the Django settings file `medisp_image_lab/settings.py` and add the newly created app.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'image_processing',
]
```


### Run the server

```bash
python manage.py runserver
```

Open a browser:

```
http://127.0.0.1:8000
```

You should see the Django welcome page.

---

## 3. Frontend Setup (React)

Open a new terminal and go to the frontend:

```bash
cd ~/VsProjects/medisp-image-lab/frontend
```

### Create the React app (if not already created)

```bash
node -v
npm -v
sudo apt update
sudo apt install nodejs npm
cd ~/VsProjects/medisp-image-lab/frontend
npx create-react-app .
```

### Start the frontend

```bash
npm start
```

Open a browser:

```
http://localhost:3000
```

You should see the React default page.

---


## 4. Make Your First Change

### React

Open:

```
frontend/src/App.js
```

Replace the content with:

```jsx
function App() {
  return <h1>Hello Medisp Lab 🚀</h1>;
}

export default App;
```

Save the file.

The page should update automatically.

---

### Django (optional)

Edit any response or template and restart the server if needed.

---

## 🧠 Key Concepts

- Backend and frontend run independently  
- Virtual environments isolate Python dependencies  
- React provides instant feedback on changes  
- Git allows us to manage versions of our project  

---

## ✅ Done Criteria

- Repository cloned  
- Day 1 branch checked out  
- Django server running  
- React app running  
- First change visible in browser  

---

## 🎉 That’s it for Day 1

You now have a working full-stack environment.

Next time, we start connecting things together.
