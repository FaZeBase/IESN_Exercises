nb_lignes = int(input("Combien de lignes ? :"))
nb_colonnes = int(input("Combien de colonnes ? :"))

def afficher_lignes_echiquier() :
    print("#_" * nb_lignes)

def afficher_lignes_alternate() :
    print("_#" * nb_lignes)


def afficher_echiquier() :
    global nb_colonnes
    while nb_colonnes // 2 > 0 :
        afficher_lignes_echiquier()
        afficher_lignes_alternate()
        nb_colonnes -= 2

afficher_echiquier()
