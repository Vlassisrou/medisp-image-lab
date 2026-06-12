FROM python:3.12-slim

WORKDIR /app

# Αντιγραφή των requirements για εγκατάσταση
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Αντιγραφή όλου του κώδικα του backend
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]