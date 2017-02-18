#!/usr/bin/env python
import sys

prev_word          = "  "                #inicializar prev_word
months             = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Nov','Dec']

dates_to_output    = [] #una lista vacia para manejar fechas para una palabra
day_cnts_to_output = [] #una lista vacia para contadores de fechas 

line_cnt           = 0  #contador de lineas

for line in sys.stdin:
    line       = line.strip()       #quita retorno de carro
    key_value  = line.split('\t')   #separa linea en clave valor
    line_cnt   = line_cnt+1     

    curr_word  = key_value[0]         #clave es primer item
    value_in   = key_value[1]         #clave es segundo item

    if curr_word != prev_word:

        if line_cnt>1:
	    for i in range(len(dates_to_output)):  #loop entre fechas
	         print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))
            #reiniciar listas
	    dates_to_output   =[]
            day_cnts_to_output=[]
        prev_word         =curr_word  #actualiza prev_word

    if (value_in[0:3] in months): 

        date_day =value_in.split() #separa el valor en fecha y contador
        
        dates_to_output.append(date_day[0])
        day_cnts_to_output.append(date_day[1])
    else:
        curr_word_total_cnt = value_in  #si el valor es el total cuenta el primer item

for i in range(len(dates_to_output)):  #loop sobre fechas para imprimir
         print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))

