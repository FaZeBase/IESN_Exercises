print("Bienvenue dans le programme Acronis True Image")
commande = input("O, X, F, P :")
def open_file () :
    fichier = input("Nom du fichier :")
    print("Ouverture du fichier :", fichier)
    
def exit_program() :
    confirmation = input("Etes-vous sûr ? (o/n)")
    print("Merci d'avoir utilisé Acronis True Image")
    
def close_file () :
    confirmation = input("Etes-vous sûr ? (o/n)")
    print("Fichier fermé")
    
def print_file() :
    nb_impressions = input("Nombre d'impressions :")
    print("Vous avez commandé",nb_impressions, " impressions")

while commande == "O" or "X" or "F" or "P" :
    if commande == "O" :
        open_file()
    elif commande == "X" :
        exit_program()
    elif commande == "F" :
        close_file()
    elif commande == "P" :
        print_file()
    else :
        commande = input("O, X, F, P :")

        

