from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# ✅ Use DATABASE_URL if provided (Render cloud DB)
# Otherwise fall back to a local SQLite file
db_url = os.environ.get('DATABASE_URL')
if not db_url:
    db_url = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

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
    with app.app_context():
        db.create_all()  # ✅ ensures the table exists
    app.run(debug=True)
