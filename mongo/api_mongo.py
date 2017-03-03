import requests
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# realiza petición a la api
response = requests.get("http://api.open-notify.org/iss-now.json")

# recupera la response de la llamada
data = response.json()


#Instanciar Cliente
client = MongoClient() #otra opcion: client = MongoClient('localhost', 27017)
#Instanciar database
db = client['test']
#Instanciar coleccion
collection = db['issnow']

id = collection.insert_one(data).inserted_id

#Mostrar todo el contenido
cursor = collection.find({})
for document in cursor: 
    pprint.pprint(document)
