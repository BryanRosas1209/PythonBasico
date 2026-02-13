# Tublas 
mi_tubla = (2, 4)
print("Mi tupla: ", mi_tubla)

# Lista
mi_lista = [1, 3.1416, "Bryan", mi_tubla]
print("El primer elemento de mi lista: ", mi_lista[0])
print ("El cuarto elemento de mi lista: ", mi_lista[3])
print ("El tercer elemeto de mi lista: ", mi_lista[2])

# Diccionarios 
mi_diccionario = {"mi_lista": mi_lista,
                    "Nombre": "bryan",
                    "Pi": 3.1416,
                    "Tel": "6631074200"}
print ("Llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print ("Llave para mi diccionario pi", mi_diccionario["Pi"])
print ("Llave para accesar a mi diccionario tel", mi_diccionario["Tel"])

i = 0

while i < 5:
    if i == 3:
        print(i)

else: 
        print("i es ahora mayor o igual a 5")