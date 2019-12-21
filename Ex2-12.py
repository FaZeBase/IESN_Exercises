nb_secret = 420
nb_input = int(input("Nombre :"))
while nb_secret != nb_input :    
    if nb_secret > nb_input :
        print("Trop petit")
    else :
        print("Trop grand")
    nb_input = int(input("Nombre :"))

print("T'as gagné")


