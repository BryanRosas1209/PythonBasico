from Enemigo import *
from Zombie import *
from Ogro import *

zombie = Zombie(10, 1)
ogro = Ogro(20, 3)

def batalla(el: Enemigo,  e2: Enemigo):
    el.habala()
    e2.habala()

    while el.puntos_energia > 0 and e2.puntos_energia > 0:
        print("################")
        el.ataque_especial()
        e2.ataque_especial()
        print(f"{el.get_tipo_enemigo()}: quedAN {el.puntos_energia} puntos de energia")
        print(f"{e2.get_tipo_enemigo()}: quedAN {e2.puntos_energia} puntos de energia")
        print(f"Ataque: {e2.ataque}")
        el.puntos_energia -= e2.ataque
        print("==================")
        print(f"Ataque: {e2.ataque}")
        e2.puntos_energia -= e2.ataque

        print("#################")
        if el.puntos_energia > 0:
            print(f"{el.get_tipo_enemigo()} gano!!!")
        else:
            print(f"{e2.get_tipo_enemigo()} gano!!!")

        

print("====================BATALLA==========================")
batalla(zombie, ogro)
print("========================FIN DE LA BATALLA=====================")
print(f"{zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energia y ataca con {zombie.ataque}")
print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y ataca con {ogro.ataque}")
