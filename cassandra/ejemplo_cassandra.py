from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

#Valor del keyspace
KEYSPACE = "testpy"

#Instanciacion de sesion y cluster
cluster = Cluster() #cluster = Cluster(['192.168.0.1', '192.168.0.2'])
session = cluster.connect()

#Creacion de keyspace
session.execute("""
	CREATE KEYSPACE %s
	WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
	""" % KEYSPACE)
session.set_keyspace(KEYSPACE)

#Creacion de tabla personas
session.execute("""
	CREATE TABLE personas (
		id text,
		nombre text,
		direccion text,
		PRIMARY KEY (id, nombre)
	)
	""")

#Insert en personas
query = SimpleStatement("""
	INSERT INTO personas (id, nombre, direccion)
	VALUES (%(key)s, %(a)s, %(b)s)
        """, consistency_level=ConsistencyLevel.ONE)
session.execute(query, dict(key='1', a='Joan', b='Casa'))


#Select de personas
rows = session.execute("SELECT * FROM personas")
for row in rows:
	print row.id, row.nombre, row.direccion

#Borrar keyspace creado
session.execute("DROP KEYSPACE " + KEYSPACE)
