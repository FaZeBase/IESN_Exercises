nb = int(input("Je vais multiplier par quoi moi ?"))
def factorielle(nb) :
    resultat = 1
    while  nb > 1 :
        resultat *= nb
        print(resultat)
        nb -= 1

factorielle(nb)
