#!/usr/bin/python

import sys
import getpass
import os
import serial

carpeta = sys.argv[1]
tiempoDelDia = sys.argv[2]
archivo = sys.argv[3]+".txt"

path = os.getcwd()
usuario = getpass.getuser() 

directorioParaDatos='C:\\Users\\'+usuario+'\\Desktop\\CMT\\Datos\\'

directorioParaEstante = directorioParaDatos+carpeta+"\\"
directorioParaTiempoDelDia = directorioParaEstante+tiempoDelDia


if not os.path.exists(directorioParaEstante):
    os.makedirs(directorioParaEstante)
else : 
    print("Folder del " + carpeta + " ya existe en %s " % directorioParaDatos)

if not os.path.exists(directorioParaTiempoDelDia):
    os.makedirs(directorioParaTiempoDelDia)
else : 
    print("Folder de " + tiempoDelDia + " ya existe en %s " % directorioParaEstante)

direccionArchivo = directorioParaTiempoDelDia+"\\"+archivo

if not os.path.exists(direccionArchivo):
    
    print("Colectando datos por un minuto..." + "\n")
    lecturaArduino = ""
    lecturaArduino = serial.Serial('COM7', baudrate=9600, timeout=1.0)

    contador = 1
    while contador <= 60:
        
        line = lecturaArduino.readline()

        f = open(direccionArchivo, "a")
        f.write(str(line, 'utf-8'))
        contador= contador+1
    
    f.close()
    print("Datos colectados!")
else : 
    print("Archivo ya existe en %s " % direccionArchivo + "\n")
    print("Por favor ingrese nuevos parametros.")