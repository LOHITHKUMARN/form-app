from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Get DATABASE_URL from Render environment
DATABASE_URL = os.environ.get('DATABASE_URL')

if not DATABASE_URL:
    # fallback for local testing
    DATABASE_URL = 'sqlite:///local.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Entry(db.Model):
    __tablename__ = 'entry'  # ensures table name is 'entry'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return "Name and email are required!", 400

    new_entry = Entry(name=name, email=email)
    db.session.add(new_entry)
    db.session.commit()

    return render_template('success.html', name=name)

@app.route('/entries')
def entries():
    all_entries = Entry.query.all()
    return '<br>'.join([f"{e.name} - {e.email}" for e in all_entries])

if __name__ == '__main__':
    # For local testing
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
