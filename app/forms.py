from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    correo_electronico = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirmar_contrasena = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('contrasena', message='Las contraseñas deben coincidir.')])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()])
    numero_telefono = StringField('Número de Teléfono', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    genero = SelectField('Género', choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], validators=[DataRequired()])
    ocupacion = StringField('Ocupación', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    correo_electronico = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
