#!/usr/bin/env python
import sys

for line in sys.stdin:
    line       = line.strip()   #quita retorno de carro
    key_value  = line.split(",")   #separa linea en clave valor
    key_in     = key_value[0].split(" ")   #clave será el primer item
    value_in   = key_value[1]   #valor el segundo

    #print key_in
    if len(key_in)>=2:           #si el registro tiene fecha y palabra en clave
        date = key_in[0]      #obtiene fecha y palabra
        word = key_in[1]
        value_out = date+" "+value_in     #concatena valores
        print( '%s\t%s' % (word, value_out) )  #imprime
    else:   #clave solo tiene palabra
        print( '%s\t%s' % (key_in[0], value_in) )  #imprime

