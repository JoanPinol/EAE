# coding=utf-8
# Indicamos que vamos a utilizar la librería tweepy que hemos instalado 
import tweepy 

# El siguiente paso es indicar los datos de conexión que hemos creado en el primer apartado del documento ( “creación de aplicación en Twitter” ) 
consumer_key = "your_consumer_key_here" 
consumer_secret = "your_consumer_secret_here" 
access_token = "your_access_token_here" 
access_token_secret = "your access_token_secret_here"
 
# Nos conectamos al Api de Twitter 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# Recuperamos nuestros datos en Twitter 
me = api.me()

# Mostrar datos del usuario en twitter
print "Nombre: " + me.screen_name 
print "Descripcion: " + me.description 
print "Numero de amigos: " + str(me.friends_count)

## parámetros de búsqueda en la api
key = "messi"
tweet_count = 100
tweet_lang = "es"
tweet_since="2017-03-01"
tweet_until="2017-04-30"

#iteramos por todas las páginas de la respuesta
for pagina in tweepy.Cursor(api.search, q= key, lang=tweet_lang, count=tweet_count,  
			include_entities=True, since=tweet_since, until=tweet_until).pages():  
	#para cada página, iteramos por sus tweets
	for tweet in pagina:
		#mostramos en pantalla la info de cada tweet
		print tweet.text.encode('utf8') 
		print "Favoritos: " + str(tweet .favorite_count) 
		print "Autor: " + str(tweet .author.profile_use_background_image) 
		print tweet.created_at 
		print tweet.author.name.encode('utf8')
		print "\n" #Ponemos una separacion entre cada mensaje


