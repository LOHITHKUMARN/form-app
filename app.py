from flask import Flask, render_template, request, redirect, send_file, Response
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import io

app = Flask(__name__)

# DATABASE_URL from Render
DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    DATABASE_URL = 'sqlite:///local.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Entry(db.Model):
    __tablename__ = 'entry'
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

@app.route('/export_csv')
def export_csv():
    try:
        all_entries = Entry.query.all()
        if not all_entries:
            return "No entries to export.", 200

        # Create CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['ID', 'Name', 'Email'])
        for entry in all_entries:
            writer.writerow([entry.id, entry.name, entry.email])

        output.seek(0)
        return Response(
            output,
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment;filename=entries.csv"}
        )
    except Exception as e:
        return f"Error generating CSV: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
