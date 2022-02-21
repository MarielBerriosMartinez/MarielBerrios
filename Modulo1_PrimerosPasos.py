# program.py
from numpy import product


sum = 1 + 2
print (sum)

print ('Hola desde la consola')
# Impresión de pantalla print ('Hola desde la consola')


sum = 1+2 # 3
product = sum*2
print (product)


# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)
print (type(distancia_a_alfa_centauri))

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())
print("Today's date is: " + str(date.today()))

# Escribe tu código aquí
print ("Estoy iniciando python en el programa Launch X")
name = input("Indrouzca su nombre")
print ("Les envia saludos" + name)

#Trabajar con números
print ('Calculadora')
first_number = input ("Introduzca el primer número")
second_number = input ("Introduzca el segundo número")
print(first_number + second_number) 

#Para que haga la suma de numeros deberia imprimir asi
print(int (first_number) + int(second_number))
