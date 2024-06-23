from flask import Flask, render_template, request, redirect, url_for, session
from config import config
from DataBase import dataBase

app = Flask(__name__)

app.secret_key = config.flask_key
app.template_folder = 'templates'
app.static_folder ='static'

@app.route('/')
def index():
    return render_template('index.html')

#rutas de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = dataBase.create_connection()
        user = dataBase.login_user(conn, username, password)

        if user:
            session['logged_in'] = True
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect('/home')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        if session.get('logged_in'):
            return redirect('/home')
        return render_template('login.html')

#rutas de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        birth_date = request.form['birth_date']
        address = request.form['address']
        job = request.form['job']

        conn = dataBase.create_connection()
        dataBase.register_user(conn, username, password, first_name, last_name, email, phone_number, birth_date, address, job)

        return redirect(url_for('login'))
    else:
        if session.get('logged_in'):
            return redirect('/home')
        return render_template('register.html')
#ruta de cerrar sesión
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(
        host=config.debug_host,
        port=config.debug_port,
        debug=config.debug_debug
    )
 