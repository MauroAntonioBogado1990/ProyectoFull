#creacion de la base de datos

import datetime as _dt
import sqlalchemy as _sql

import database as _database

class Users(_database.Base):
    __tablename__ = "users"
    id  = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name: _sql.Column(_sql.String, index=True)
    lastname: _sql.Column(_sql.String, index=True)    
    phone = _sql.Column(_sql.String, index=True)
    address: _sql.Column(_sql.String, index=True)
    email: _sql.Column(_sql.String, index=True, unique=True)
    phone_number: _sql.Column(_sql.String, index=True, unique=True)
    date_create: _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
