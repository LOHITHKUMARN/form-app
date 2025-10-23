from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Render provides DATABASE_URL environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    new_entry = Entry(name=name, email=email)
    db.session.add(new_entry)
    db.session.commit()
    return render_template('success.html', name=name)

@app.route('/entries')
def entries():
    all_entries = Entry.query.all()
    return '<br>'.join([f"{e.name} - {e.email}" for e in all_entries])

if __name__ == '__main__':
    app.run(debug=True)
