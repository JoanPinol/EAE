import requests
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

# Make the same request we did earlier, but with the coordinates of San Francisco instead.
response = requests.get("http://api.open-notify.org/iss-now.json")

# Get the response data as a python object.  Verify that it's a dictionary.
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
