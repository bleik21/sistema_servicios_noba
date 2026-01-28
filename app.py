from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import bcrypt

app = Flask(__name__)
app.secret_key = 'clave_secreta_noba_2026'

# =================================================
# ⚠️ BASE DE DATOS DESACTIVADA TEMPORALMENTE
# (En Render no existe MySQL localhost)
# Más adelante conectaremos a una BD externa
# =================================================

# import mysql.connector
# def get_db_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="tu_base_de_datos"
#     )

# =================================================
# RUTAS DE NAVEGACIÓN
# =================================================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/registro')
def registro_page():
    return render_template('registro.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return f"Bienvenido al Panel de Control de NOBA, {session.get('nombre')}."
    return redirect(url_for('login_page'))

# =================================================
# LOGIN FACIAL (SIMULADO)
# =================================================

@app.route('/login_facial', methods=['POST'])
def login_facial():
    session['user_id'] = 999
    session['nombre'] = "Usuario Biométrica"
    return jsonify({"status": "success", "message": "Identidad validada"}), 200

# =================================================
# LOGIN NORMAL (SIMULADO SIN BD)
# =================================================

@app.route('/ejecutar_login', methods=['POST'])
def ejecutar_login():
    email = request.form.get('email')
    password = request.form.get('password')

    # ⚠️ Simulación temporal sin BD
    if email == "admin@noba.com" and password == "1234":
        session['user_id'] = 1
        session['nombre'] = "Administrador NOBA"
        return redirect(url_for('dashboard'))
    else:
        return "Credenciales incorrectas (modo demo)", 401

# =================================================
# REGISTRO (SIMULADO)
# =================================================

@app.route('/procesar_registro', methods=['POST'])
def procesar_registro():
    # En producción aquí irá la BD
    return redirect(url_for('login_page'))

# =================================================
# LOGOUT
# =================================================

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# =================================================
# MAIN
# =================================================

if __name__ == '__main__':
    app.run(debug=True)
