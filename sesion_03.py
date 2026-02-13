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

mi_lista_2 = {"lunes","martes","miercoles","jueves","viernes"}

for i in mi_lista_2:
     if i != "lunes":
        print(f"Feliz: {i}" )