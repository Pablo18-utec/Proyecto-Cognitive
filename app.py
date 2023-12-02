
from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import secrets

app = Flask(_name_, template_folder='template')
app.secret_key = secrets.token_hex(16)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'loginpoo20232'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

# Función de login
@app.route('/acceso-login', methods=["POST"])
def login():
    if request.method == 'POST' and 'txtusuario' in request.form and 'txtpassword' in request.form:
        _correo = request.form['usuario']
        _password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND password = %s', (_correo, _password,))
        account = cur.fetchone()

        cur.close()

        if account:
            session['logueado'] = True
            session['id'] = account['id']
            return render_template("usuario.html", mensaje="Inicio de sesión exitoso")
        else:
            return render_template("index.html", mensaje="Correo o contraseña incorrectos")

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=3306, threaded=True)