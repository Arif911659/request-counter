from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///counter.db'
db = SQLAlchemy(app)

class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=0)

@app.route('/')
def index():
    counter = Counter.query.first()
    if counter is None:
        counter = Counter(count=0)
        db.session.add(counter)
    counter.count += 1
    db.session.commit()

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Request Counter</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f8ff;
            }
            .container {
                text-align: center;
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #2c3e50;
            }
            .count {
                font-size: 4rem;
                color: #3498db;
                margin: 1rem 0;
            }
            .refresh-btn {
                background-color: #2ecc71;
                color: white;
                border: none;
                padding: 0.5rem 1rem;
                font-size: 1rem;
                cursor: pointer;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            .refresh-btn:hover {
                background-color: #27ae60;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Browser Request Counter</h1>
            <p>This page has been accessed:</p>
            <div class="count" aria-live="polite">{{ counter.count }} times</div>
            <button class="refresh-btn" onclick="location.reload()">Refresh Count</button>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, counter=counter)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)

