import bcrypt
import sqlite3
from flask import Flask, render_template_string
from flask import request

# Configuración de Flask
app = Flask(__name__)

# Crear la base de datos y tabla si no existe
def crear_bd():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY, nombre TEXT, contraseña TEXT)''')
    conn.commit()
    conn.close()

# Función para almacenar los datos del usuario con contraseña hash
def almacenar_usuario(nombre, contraseña):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    # Generar el hash de la contraseña
    hash_contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
    c.execute("INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)", 
              (nombre, hash_contraseña))
    conn.commit()
    conn.close()

# Función para validar usuario y contraseña
def validar_usuario(nombre, contraseña):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT contraseña FROM usuarios WHERE nombre=?", (nombre,))
    stored_password = c.fetchone()
    conn.close()
    if stored_password is None:
        return False
    # Verificar si el hash de la contraseña coincide
    return bcrypt.checkpw(contraseña.encode('utf-8'), stored_password[0])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        contraseña = request.form["contraseña"]
        # Validar las credenciales de 'Marcelo Peralta'
        if nombre == "Marcelo Peralta" and contraseña == "cisco123!":
            if validar_usuario(nombre, contraseña):
                return f"¡Bienvenido, {nombre}!"
            else:
                return "¡Credenciales incorrectas!"
        else:
            return "El usuario no es válido."

    return '''
        <form method="POST">
            Nombre de usuario: <input type="text" name="nombre"><br>
            Contraseña: <input type="password" name="contraseña"><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    '''

if __name__ == "__main__":
    # Crear la base de datos si no existe
    crear_bd()
    # Almacenar usuario y contraseña "Marcelo Peralta" con su hash
    almacenar_usuario("Marcelo Peralta", "cisco123!")
    app.run(debug=True, host="127.0.0.1", port=5800)
