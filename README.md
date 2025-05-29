# candidate-tracker-api
A Django REST Framework-based API for tracking job applicants. This project provides endpoints to create, update, delete, and search candidates based on name relevance. Built as part of an ATS (Applicant Tracking System) assignment, it demonstrates efficient use of Django ORM, clean API design, and search functionality optimized for performance.

# 🧪 Candidate Search API (Django REST Framework)


## ✅ Features

* Create, update, delete candidates.
* Search candidates by name.
* Relevancy-based sorting (number of matched words).
* Uses Django ORM only — no Python-side filtering or sorting.

---

## 📦 Tech Stack

* Python 3.8+
* Django 4.x
* Django REST Framework

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Singh-Sg/candidate-tracker-api
cd candidate-api
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```
asgiref==3.8.1
Django==5.2.1
django-rest-framework==0.1.0
djangorestframework==3.16.0
sqlparse==0.5.3

```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

API will be available at:

📍 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🗂️ API Endpoints

### 🔹 Base URL

```
http://127.0.0.1:8000/candidates/
```

---

### 📌 Create a Candidate

**POST** `/create/`

**Request Body (JSON)**:

```json
{
  "name": "Ajay Kumar Yadav",
  "age": 30,
  "gender": "Male",
  "email": "ajay@example.com",
  "phone_number": "1234567890"
}
```

---

### 📌 Update a Candidate

**PUT** `/update/<id>/`

**Example**:
`PUT /api/candidates/update/1/`

**Request Body**:

```json
{
  "name": "Ajay Kumar",
  "age": 31,
  "gender": "Male",
  "email": "ajayk@example.com",
  "phone_number": "1234567890"
}
```

---

### 📌 Delete a Candidate

**DELETE** `/delete/<id>/`

**Example**:
`DELETE /api/candidates/delete/1/`

---

### 📌 Search Candidates by Name

**GET** `/search/?q=search terms`

**Example**:
`GET /api/candidates/search/?q=Ajay Kumar Yadav`

**Response (sorted by relevance)**:

```json
[
  { "id": 1, "name": "Ajay Kumar Yadav", ... },
  { "id": 2, "name": "Ajay Kumar", ... },
  { "id": 3, "name": "Ajay Yadav", ... },
  { "id": 4, "name": "Kumar Yadav", ... },
  { "id": 5, "name": "Ramesh Yadav", ... },
  { "id": 6, "name": "Ajay Singh", ... }
]
```

---