# -*- coding: utf-8 -*-

from flask_login import login_user, logout_user, login_required
from flask import render_template, redirect, url_for, flash, request, session
from . import app, db, login_manager
from .models import Usuario, Prestamo, Transaccion
from .forms import RegistroForm, LoginForm  # Importa tus formularios adecuadamente

@app.route('/')
def index():
    # Aquí puedes mostrar información general sobre el fondo de ahorro y crédito
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()  # Crea una instancia del formulario de registro

    if form.validate_on_submit():
        # Procesar el formulario y crear un nuevo usuario en la base de datos
        nuevo_usuario = Usuario(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            correo_electronico=form.correo_electronico.data,
            contrasena=form.contrasena.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            numero_telefono=form.numero_telefono.data,
            direccion=form.direccion.data
            # Agrega más campos según tus necesidades
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))  # Redirige al usuario a la página de inicio de sesión

    return render_template('registro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Crea una instancia del formulario de inicio de sesión

    if form.validate_on_submit():
        # Validar las credenciales y permitir el inicio de sesión
        usuario = Usuario.query.filter_by(correo_electronico=form.correo_electronico.data).first()
        if usuario and usuario.contrasena == form.contrasena.data:
            login_user(usuario)
            session['usuario'] = usuario.nombre  # Guarda el nombre de usuario en la sesión
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('panel_usuario'))  # Redirige al usuario al panel de usuario

        flash('Inicio de sesión fallido. Verifica tus credenciales.', 'danger')

    return render_template('login.html', form=form)


@app.route('/panel-usuario')
@login_required
def panel_usuario():
    # Vista del panel de usuario para usuarios autenticados
    return render_template('panel_usuario.html', nombre_usuario=session.get('usuario'))

@app.route('/solicitud-prestamo', methods=['GET', 'POST'])
@login_required
def solicitud_prestamo():
    # Lógica para permitir a los usuarios solicitar un préstamo
    if request.method == 'POST':
        # Procesar la solicitud de préstamo y registrarla en la base de datos
        flash('¡Solicitud de préstamo enviada con éxito!', 'success')
        return redirect(url_for('panel_usuario'))
    return render_template('solicitud_prestamo.html')

@app.route('/historial-transacciones')
@login_required
def historial_transacciones():
    # Vista del historial de transacciones para usuarios autenticados
    return render_template('historial_transacciones.html')

@app.route('/cerrar-sesion')
@login_required
def cerrar_sesion():
    logout_user()
    session.pop('usuario', None)  # Elimina la variable de sesión 'usuario'
    flash('¡Sesión cerrada con éxito!', 'success')
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
