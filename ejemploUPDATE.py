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

# Preparamos el query SQL para modificar el registro
sql = "UPDATE EMPLEADO SET EDAD = EDAD + 1 WHERE SALARIO = 2000"
try:
   # Ejecutamos el comando
   cursor.execute(sql)
   # Efectuamos los cambios en la base de datos
   bd.commit()
except:
   # Si se genero algún error revertamos la operación
   bd.rollback()

# Nos desconectamos de la base de datos
bd.close()
