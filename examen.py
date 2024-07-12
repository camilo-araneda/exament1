import random
import csv
from random import randint

sueldo=[]
azar=randint(1,100)
sueldo=[0]

from random import randint


def clasificacion_sueldo():
    trabajadores=["Juan Perez","Maria Garcia","Carlos lópez","Ana Martinez","Pedro Rodriguez","Laura Hernández","Miguel Sanchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
    conSueldos=[]


trabajadores=["Juan Perez","Maria Garcia","Carlos lópez","Ana Martinez","Pedro Rodriguez","Laura Hernández","Miguel Sanchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]


conSueldos=[]
for t in trabajadores:
    trabajadores.append (("Nombre de trabajador":t,"Sueldo":randint(300000,2500000)))
    print(conSueldos)

sueldosTotales=[]
    
for i in trabajadores:
  sueldo.append(300000,2500000)
  sueldo=[]
  sueldo.append()

def asignar_sueldos():
    for i in trabajadores:
        print("Nombre",(trabajadores))
        print("Sueldo entre 300000,2500000")      


opc=6


while True:
    print("---------------------------------------------")
    print("1.-Asignar Sueldos Aleatorios ")
    print("2.-Clasificar Sueldos ")
    print("3.-Ver Estadisticas ")
    print("4.-Reporte de Sueldo ")
    print("5.-Salir del Programa")
    print("---------------------------------------------")
    op=int(input("Escoja una opcion "))
    match op:
        case 1:
            input(print("Escriba su nombre:"))
            int(input("Escriba su sueldo entre 300000 , 2500000"))
            
        case 2:
            print(trabajadores,sueldo)
        
        case 3:
            print(sueldo)
            print(sueldo)
            print(sueldo)
            print(sueldo)
            
            
            
        case 5:
            print("Finalizando programa...")
            print("Desarrollado por camilo araneda")
            print("RUT 21.491.000-4")
            break