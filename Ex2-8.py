print("Bienvenue dans le programme Acronis True Image")
commande = input("O, X, F, P :")

if commande == "O" :
    fichier = input("Nom du fichier :")
    print("Ouverture du fichier :", fichier)
elif commande == "X" :
    confirmation = input("Etes-vous sûr ? (o/n)")
    print("Merci d'avoir utilisé Acronis True Image")
elif commande == "F" :
    confirmation = input("Etes-vous sûr ? (o/n)")
    print("Fichier fermé")
elif commande == "P" :
    nb_impressions = input("Nombre d'impressions :")
    print("Vous avez commandé",nb_impressions, " impressions")
else :
    commande = input("O, X, F, P")
