from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['DATABASE'] = os.path.join(app.instance_path, 'app.sqlite')

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

DATABASE = app.config['DATABASE']

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    cur.close()

def create_user(username, email, password):
    execute_db("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", (username, email, password))

def get_user_by_email(email):
    return query_db("SELECT * FROM user WHERE email = ?", (email,), one=True)

def create_post(title, content, user_id):
    execute_db("INSERT INTO post (title, content, user_id) VALUES (?, ?, ?)", (title, content, user_id))

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS post (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id)
            )
        ''')
        db.commit()

@app.route("/")
@app.route("/home")
def home():
    posts = query_db("SELECT * FROM post")
    return render_template('index.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        try:
            create_user(username, email, password)
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists', 'danger')
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        create_post(title, content, session['user_id'])
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html')

# Initialize the database
init_db()

if __name__ == '__main__':
    app.run(debug=True)
