#!/usr/bin/python
# coding=utf-8

import MySQLdb

host = "localhost"
user = "testuser"
password = "pwd"
database = "test"

# crear conexión con bdd
bd = MySQLdb.connect("localhost","testuser","pwd","test")

# inicializar cursor
cursor = bd.cursor()

# ejecutar una query con el método execute del cursor
cursor.execute("SELECT nombre FROM alumnos")

# extraer una fila con el método fetchone
data = cursor.fetchone()

print "Datos : %s " % data

# desconexión de la bdd
bd.close()
