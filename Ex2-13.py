nb_secret = 420
nb_input = int(input("Nombre :"))
nb_essais = 5
while nb_secret != nb_input and nb_essais > 0 :
    if nb_secret > nb_input :
        print("Trop petit")
    else :
        print("Trop grand")
    nb_essais -= 1
    if nb_essais > 0:
        nb_input = int(input("Nombre :"))

    print(nb_essais)

if nb_essais > 0 :
    print("T'as gagné")
else :
    print("T'as perdu")
