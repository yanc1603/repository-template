import os
from flask import Flask, request, jsonify, session, redirect, url_for, send_from_directory
from models import db, User
import bcrypt
from flasgger import Swagger

app = Flask(__name__, static_folder='public', static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key-just-for-demo'

db.init_app(app)
swagger = Swagger(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: User registered successfully
      400:
        description: User already exists or invalid input
    """
    data = request.get_json()
    if not data:
        data = request.form

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Please provide username and password.'}), 400

    if not isinstance(username, str):
         return jsonify({'error': 'Invalid username.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Registration successful! Please log in.'})

@app.route('/login', methods=['POST'])
def login():
    """
    Login a user
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
      400:
        description: Invalid input
    """
    data = request.get_json()
    if not data:
        data = request.form

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Please provide username and password.'}), 400
    
    if not isinstance(username, str):
         return jsonify({'error': 'Invalid username.'}), 400

    user = User.query.filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
        session['user_id'] = user.id
        session['username'] = user.username
        return jsonify({'success': True, 'redirect': '/dashboard'})
    else:
        return jsonify({'error': 'Invalid password.'}), 401

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f'<h1>Welcome, {session["username"]}!</h1><a href="/logout">Logout</a>'
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
