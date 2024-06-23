#database usando sqlite3
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('DataBase/database.db')
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

#crear la tabla de usuarios , contraseñas , nombre y apellido, email, telefono, fecha de nacimiento, dirección,oficio
def create_users_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        phone_number TEXT NOT NULL UNIQUE,
                        birth_date TEXT NOT NULL,
                        address TEXT NOT NULL,
                        job TEXT NOT NULL
                    )''')
        print("Table created successfully")
    except Error as e:
        print(e)
#función para registrar un nuevo usuario
def register_user(conn, username, password, first_name, last_name, email, phone_number, birth_date, address, job):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, first_name, last_name, email, phone_number, birth_date, address, job) VALUES (?,?,?,?,?,?,?,?,?)",
                  (username, password, first_name, last_name, email, phone_number, birth_date, address, job))
        conn.commit()
        print("User registered successfully")
    except Error as e:
        print(e)
#función para iniciar sesión
def login_user(conn, username, password):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username =? AND password =?", (username, password))
        user = c.fetchone()
        if user:
            print("User logged in successfully")
            return user
        else:
            print("User not found")
    except Error as e:
        print(e)
#función para actualizar los datos de un usuario
def update_user(conn, id, username, password, first_name, last_name, email, phone_number, birth_date, address, job):
    try:
        c = conn.cursor()
        c.execute("UPDATE users SET username =?, password =?, first_name =?, last_name =?, email =?, phone_number =?, birth_date =?, address =?, job =? WHERE id =?",
                  (username, password, first_name, last_name, email, phone_number, birth_date, address, job, id))
        conn.commit()
        print("User updated successfully")
    except Error as e:
        print(e)
#función para eliminar un usuario
def delete_user(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE id =?", (id,))
        conn.commit()
        print("User deleted successfully")
    except Error as e:
        print(e)
