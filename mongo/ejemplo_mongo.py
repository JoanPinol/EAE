from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

#Instanciar Cliente
client = MongoClient() #otra opcion: client = MongoClient('localhost', 27017)
#Instanciar database
db = client['got']
#Instanciar coleccion
collection = db['families']

print "Contenido de families"
#Mostrar todo el contenido
cursor = collection.find({})
for document in cursor: 
    pprint.pprint(document)

#Instanciar nuevo objeto
family = {'name':'Lannister', 'procedence':'Lannisport', 'members':[3]}
#Insertar nuevo objeto y recuperar ID
lannisid = db.families.insert_one(family).inserted_id

print "Contenido despues del insert:"
#Mostrar todo el contenido
cursor = collection.find({})
for document in cursor: 
    pprint.pprint(document)

#Borrar registro insertado
result = db.families.delete_one({'_id': ObjectId(lannisid)})

print "Contenido despues del delete:"
#Mostrar todo el contenido
cursor = collection.find({})
for document in cursor: 
    pprint.pprint(document)
