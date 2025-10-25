# Flask Form App

A simple Flask web application to collect user information (name and email) and store it in a PostgreSQL database hosted on Render. Users can submit their details via a form, and view all submitted entries in a table.

---

## Live Site

- [Form Submission](https://form-app2-3.onrender.com)  
- [View Entries](https://form-app2-3.onrender.com/e_csv)

---

## Features

- User form for collecting **name** and **email**.
- Saves data to **PostgreSQL** database.
- View all submitted entries in a neat table.
- Fully deployed on **Render**.
- Supports local SQLite for testing.

---

## Technologies Used

- **Python 3.13**
- **Flask**
- **Flask-SQLAlchemy**
- **PostgreSQL** (on Render)
- **HTML / Jinja2** templates

---

## Installation / Setup

1. **Clone the repository**

``bash
git clone https://github.com/your-username/flask-form-app.git
cd flask-form-app
Create a virtual environment and activate

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables

Create a .env file in the project root:

env
Copy code
DATABASE_URL=postgresql://<user>:<password>@<host>/<database>
PORT=5000
For local testing, SQLite fallback is used: sqlite:///local.db

Run the app locally

bash
Copy code
python app.py
Visit http://127.0.0.1:5000 in your browser.

Deployment on Render
Create a new Web Service on Render.

Connect your GitHub repository.

Set environment variables:

bash
Copy code
DATABASE_URL=postgresql://flask_data_db_user:<password>@<host>/flask_data_db
Deploy and your app will be live.

Usage
Go to / to submit your name and email.

Go to /view_entries to see all submissions.

Screenshots
Form Page


View Entries


Notes
Make sure the PostgreSQL database table entry exists. The app will attempt to create it automatically on startup.

For local testing, the app uses SQLite (local.db) if DATABASE_URL is not set.

