#loops


mi_lista = {1,2,3,4}

for i in mi_lista:
    print("El numero es: ", i)

resultado = 0
for i in mi_lista:
     resultado += i

print(f"El resultado de la sume de mi lista es: {resultado}")
for i in range(2, 8):
     print(i)

mi_lista_2 = ["lunes","martes","miercoles","jueves","viernes"]

contador = 0

while contador < 3:
    for i in mi_lista_2:
        if i != "lunes":
            print(i)
    contador += 1


# While loop


# Practica 2
# Dada la lista mi_lista_2 = {"lunes","martes","miercoles","jueves","viernes"}
# Imprimer Cada ekemento de la lista 3 veces y cuando sea lunes no lo incluyas
# Pista usa los dos tupos loops while y for en ek mismo programa ára lograrlo 
# Resultado
# Martes
# Miercoles
# jueves
# viernes
# martes 
# miiercoles 
# jueves
# viernes
