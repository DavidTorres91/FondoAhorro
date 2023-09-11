from app import db
from flask_login import UserMixin
from sqlalchemy import Boolean

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    correo_electronico = db.Column(db.String(255), unique=True)
    contrasena = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    numero_telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    cuentas_ahorro = db.relationship('CuentaAhorro', backref='usuario', lazy='dynamic')
    prestamos = db.relationship('Prestamo', backref='usuario', lazy='dynamic')
    sesiones = db.relationship('RegistroSesion', backref='usuario', lazy='dynamic')
    activo = db.Column(Boolean, default=True)

    def is_active(self):
        return self.activo

class RegistroSesion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    fecha_inicio = db.Column(db.DateTime)
    fecha_cierre = db.Column(db.DateTime)
    duracion = db.Column(db.Time)
    direccion_ip = db.Column(db.String(15))

class CuentaAhorro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    saldo = db.Column(db.Numeric(10, 2))
    fecha_apertura = db.Column(db.Date)
    transacciones = db.relationship('Transaccion', backref='cuenta_ahorro', lazy='dynamic')

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    monto_prestamo = db.Column(db.Numeric(10, 2))
    tasa_interes = db.Column(db.Numeric(5, 2))
    plazo_meses = db.Column(db.Integer)
    estado = db.Column(db.String(20))
    fecha_solicitud = db.Column(db.Date)
    fecha_aprobacion = db.Column(db.Date)
    fecha_pago = db.Column(db.Date)
    transacciones = db.relationship('Transaccion', backref='prestamo', lazy='dynamic')

class Transaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    tipo = db.Column(db.String(20))
    monto = db.Column(db.Numeric(10, 2))
    fecha_hora = db.Column(db.DateTime)
    descripcion = db.Column(db.Text)
    cuenta_ahorro_id = db.Column(db.Integer, db.ForeignKey('cuenta_ahorro.id'))
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamo.id'))
