import math
nb_input = int(input("Nombre :"))

def squared_tester() :
    global nb_input
    if math.sqrt(nb_input) % 1 == 0 :
        print("Ce nombre est un carré")
    else :
        print("Ce nombre n'est pas un carré")

squared_tester()
