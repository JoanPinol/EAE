#!/usr/bin/env python
import sys

#para todos los registros
for line in sys.stdin:
    line       = line.strip()   #eliminar retorno de carro
    key_value  = line.split(",")   #separar linea en clave valor
    key        = key_value[0]   #asignar clave
    value      = key_value[1]   #asignar valor

    #imprimir registro
    if value == "ABC" or value.isdigit():
        print( '%s\t%s' % (key, value) )

