from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de Flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Usuario {self.username}>'

# Formularios de WTF Flask
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Rutas para manejar las solicitudes HTTP
@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/logo')
def logo():
    return render_template('logo.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Usuario.query.filter_by(username=username).first()  # Busca el usuario por username
        if user and check_password_hash(user.password, password):  # Verifica la contraseña
            flash('Login exitoso')  # Mensaje de éxito
            return redirect(url_for('inicio'))
        else:
            flash('Credenciales inválidas. Inténtalo de nuevo.')  # Mensaje de error
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
