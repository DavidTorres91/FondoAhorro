# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    correo_electronico = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    contrasena = PasswordField('Contraseña', validators=[DataRequired()])
    confirmar_contrasena = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('contrasena', message='Las contraseñas deben coincidir.')])
    numero_telefono = StringField('Número de Teléfono', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    submit = SubmitField('Registrarse')
