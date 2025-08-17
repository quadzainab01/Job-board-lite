# Job Board Lite

## Overview
Job Board Lite is a simplified job board web application built with Django.  
It allows recruiters to post job openings and job seekers to view and apply for them.  
The project demonstrates core Django functionality including models, views, forms, templates, and API endpoints.

## Features
- User registration and login system with role distinction (Recruiter vs Job Seeker)  
- Recruiters can:
  - Post job vacancies  
  - View applications submitted for their jobs via the Admin panel  
- Job Seekers can:
  - View job listings  
  - Apply for jobs using a simple form (name, email, cover note)  
- Form validation and basic UI feedback

## Tech Stack
- Backend: Django, Django REST Framework (DRF)  
- Frontend: Django templates, Bootstrap/TailwindCSS (depending on time)  
- Database: SQLite (default, can be swapped with PostgreSQL)  
- Deployment: Render.com (free plan)

## Project Structure

job-board-lite/
│
├── manage.py
├── requirements.txt
├── .gitignore
├── users/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── templates/
    ├── base.html
    ├── users/
    │   ├── login.html
    │   └── register.html
    └── jobs/
        ├── job_list.html
        ├── job_detail.html
        ├── post_job.html
        └── apply_job.html


## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/your-username/job-board-lite.git
cd job-board-lite

2. Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Apply migrations:
python manage.py migrate

4. Run the development server:
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

Next Steps
1. Implement full API endpoints for job posts and applications

2. Add frontend pages for recruiters and job seekers

3. Deploy the application to Render.com

License:
This project is open-source and available under the MIT License.