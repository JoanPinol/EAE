#!/usr/bin/python
# coding=utf-8

import MySQLdb

# Definimos variables de acceso a BDD
host = "localhost"
user = "testuser"
password = "pwd"
database = "test"

# Crear conexión con bdd
bd = MySQLdb.connect(host,user,password,database)

# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()

# Creamos la tabla empleado
sql = """CREATE TABLE EMPLEADO (
	NOMBRE  CHAR(20) NOT NULL,
	APELLIDO  CHAR(20),
	EDAD INT,
	SEXO CHAR(1),
	SALARIO FLOAT )"""

cursor.execute(sql)

# Nos desconectamos de la base de datos
bd.close()
