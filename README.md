
# Course Application

Full-stack course platform with React frontend and Django backend. Manages users, courses, videos, payments, and user-course enrollments.

## Tech Stack

- Frontend: React, React Router, Axios (or fetch), Redux (optional)
- Backend: Django, Django REST Framework (DRF)
- Database: PostgreSQL (or any supported by Django)
- Authentication: JWT (e.g., djangorestframework-simplejwt) or session-based
- Deployment: Docker (optional), Nginx, Gunicorn

## Project Structure

```
course-app/
├── backend/                # Django project and apps
│   ├── manage.py
│   ├── requirements.txt
│   ├── django_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── users/
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── courses/
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── videos/
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── payments/
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   ├── usercourses/
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   └── urls.py
│   │   └── learnings/        # or include in courses
│   │       ├── models.py
│   │       ├── serializers.py
│   │       ├── views.py
│   │       └── urls.py
│   └── docker/               # optional Docker setup
├── frontend/                 # React app
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── store/              # if using Redux
│   │   ├── services/           # api clients
│   │   ├── App.js
│   │   ├── index.js
│   │   └── routing/
│   ├── public/
│   └── package.json
├── README.md
└── docker-compose.yml        # optional
```

## Database Entities (Overview)

- Users
  - email
  - password
  - first_name
  - last_name
  - active
  - date
  - description
- Courses
  - name
  - description
  - price
  - discount
  - active
  - date
  - thumbnail
  - resource
  - course_length
- Videos
  - resource
  - sequential_number (serial_Number)
  - url
  - isPreview
  - title
  - course (FK)
- Tags
  - tag
  - course (FK)
- Prerequisites
  - prerequisite
  - course (FK)
  - discount
- Learnings
  - course (FK)
  - learning (FK) / content
- Payments
  - payment_id
  - request_id
  - status
  - user_course (FK)
  - date
- UserCourse
  - user (FK)
  - course (FK)
  - date

Note: Adjust field names to Pythonic conventions in Django (e.g., serial_number, is_preview, foreign keys with related_name).

## API Design (DRF)

- Authentication
  - /api/auth/login/  (obtain JWT)
  - /api/auth/register/
  - /api/auth/refresh/

- Users
  - GET /api/users/ – list
  - GET /api/users/{id}/ – retrieve
  - PUT/PATCH /api/users/{id}/ – update
  - DELETE /api/users/{id}/ – delete

- Courses
  - GET /api/courses/ – list
  - POST /api/courses/ – create
  - GET /api/courses/{id}/ – detail
  - PUT/PATCH /api/courses/{id}/ – update
  - DELETE /api/courses/{id}/ – delete

- Videos
  - GET /api/videos/
  - GET /api/videos/{id}/
  - ...

- Payments
  - POST /api/payments/ – create payment
  - GET /api/payments/{id}/

- UserCourse
  - POST /api/usercourses/ – enroll
  - GET /api/usercourses/{id}/

- Learnings, Tags, Prerequisites
  - CRUD endpoints as needed per resource

- Relationships
  - Nested or serialized representations to show course-videos, course-tags, etc.

## Frontend Architecture

- Routes
  - /login, /register
  - /courses – list
  - /courses/:id – course detail (and enroll)
  - /videos/:id – video player
  - /payments/:id – payment status
  - /profile – user profile

- State Management
  - Use React context or Redux for auth, user data, course catalog, and cart/enrollments.

- API Layer
  - Centralized API client (e.g., services/api.js) with axios/fetch
  - Interceptors for auth tokens, error handling

- Components
  - CourseCard, CourseList, VideoPlayer, VideoList
  - PaymentButton, EnrollmentBadge
  - UserProfile, Dashboard

- Styling
  - CSS Modules, Styled-Components, or Tailwind depending on preference

## Setup Instructions

- Clone the repo
- Backend
  - Navigate to backend/
  - Create virtual environment: python -m venv venv
  - Activate: source venv/bin/activate
  - Install: pip install -r requirements.txt
  - Apply migrations: python manage.py migrate
  - Create superuser: python manage.py createsuperuser
  - Run: python manage.py runserver 8000

- Frontend
  - Navigate to frontend/
  - Install: npm install
  - Run: npm start
  - Or with Yarn: yarn install && yarn start

- Environment Variables (examples)
  - Backend: DJANGO_SECRET_KEY, DJANGO_DEBUG, DATABASE_URL
  - Frontend: REACT_APP_API_BASE_URL

## Data Model Highlights

- Use foreign keys to model: 
  - Course has many Videos
  - Course has many Tags
  - Course has many Prerequisites
  - Course has many Learnings
  - User can enroll in many Courses (UserCourse)
  - Payments link Users via UserCourse

- Consider index optimization on frequently queried fields (course name, user email, payment status).


