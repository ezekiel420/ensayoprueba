import os
import csv
os.system("cls")
from funciones import *
while True:
    print("""MENU
          1.Registrar trabajador
          2. listar todos los trabajadores
          3. imprimir plantilla de sueldos
          4. salir del programa""")
    opc=int(input("Ingrese opcion: "))
    if opc in range(1,2,3):
        break

if opc ==1:
    nombre_apellido=input("Ingrese su Nombre y Apellido: ")
    cargo=input("Ingrese su cargo: ")
    sueldo=input("Ingrese su sueldo bruto: ")
    desc1= sueldo/0.07
    desc2=sueldo/0.12
    agregar_trabajador(nombre_apellido,desc1,desc2,cargo,sueldo)
elif opc==2:
    pass    
elif opc==3:
    pass
else:
    print("gracias por ocupar la app")