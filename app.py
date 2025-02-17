from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response, session, flash, get_flashed_messages
import requests
import random
import jwt
import datetime
from functools import wraps
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['EMAIL_USER'] = os.getenv('EMAIL_USER')
app.config['EMAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')

# Decorador para verificar el token JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('login'))
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

# Función para enviar el correo electrónico
def send_verification_email(to_email, code):
    msg = MIMEMultipart()
    msg['From'] = app.config['EMAIL_USER']
    msg['To'] = to_email
    msg['Subject'] = 'Código de verificación'
    body = f'Tu código de verificación es: {code}'
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(app.config['EMAIL_USER'], app.config['EMAIL_PASSWORD'])
        text = msg.as_string()
        server.sendmail(app.config['EMAIL_USER'], to_email, text)
        server.quit()
    except Exception as e:
        print(f'Error al enviar el correo: {e}')

# Ruta para servir el frontend
@app.route('/')
@token_required
def index():
    return render_template('index.html')

# Ruta para el login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        auth = request.form
        if auth and auth['username'] == 'admin' and auth['password'] == 'password':
            verification_code = random.randint(100000, 999999)
            session['verification_code'] = verification_code
            send_verification_email('nlmarchisio93@gmail.com', verification_code)
            flash('Se ha enviado un código de verificación a tu correo electrónico.')
            return redirect(url_for('verify'))
        return render_template('login.html', error='Credenciales inválidas')
    return render_template('login.html')

# Ruta para la verificación del código
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        code = request.form['code']
        if 'verification_code' in session and code == str(session['verification_code']):
            token = jwt.encode({'user': 'admin', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
            response = redirect(url_for('index'))
            response.set_cookie('token', token)
            session.pop('verification_code', None)
            return response
        flash('Código de verificación inválido')
    return render_template('verify.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('token', '', expires=0)
    return response

# Endpoint para obtener el tipo de un Pokémon según su nombre
@app.route('/pokemon/type/<name>', methods=['GET'])
@token_required
def get_pokemon_type(name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        data = response.json()
        types = [t['type']['name'] for t in data['types']]
        return jsonify({'name': name, 'types': types, 'id': data['id'], 'species_url': data['species']['url']})
    else:
        return jsonify({'error': 'Pokémon not found'}), 404

# Endpoint para obtener un Pokémon al azar de un tipo en específico
@app.route('/pokemon/random/<type>', methods=['GET'])
@token_required
def get_random_pokemon(type):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{type}')
    if response.status_code == 200:
        data = response.json()
        pokemon_list = data['pokemon']
        random_pokemon = random.choice(pokemon_list)['pokemon']['name']
        pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_pokemon}')
        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json()
            return jsonify({'type': type, 'random_pokemon': random_pokemon, 'id': pokemon_data['id'], 'species_url': pokemon_data['species']['url']})
        else:
            return jsonify({'error': 'Pokémon not found'}), 404
    else:
        return jsonify({'error': 'Type not found'}), 404

# Endpoint para obtener el Pokémon con nombre más largo de cierto tipo
@app.route('/pokemon/longest/<type>', methods=['GET'])
@token_required
def get_longest_pokemon_name(type):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{type}')
    if response.status_code == 200:
        data = response.json()
        pokemon_list = data['pokemon']
        longest_name = max(pokemon_list, key=lambda p: len(p['pokemon']['name']))['pokemon']['name']
        pokemon_response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{longest_name}')
        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json()
            return jsonify({'type': type, 'longest_name': longest_name, 'id': pokemon_data['id'], 'species_url': pokemon_data['species']['url']})
        else:
            return jsonify({'error': 'Pokémon not found'}), 404
    else:
        return jsonify({'error': 'Type not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

