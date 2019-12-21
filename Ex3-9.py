def invert_minuscule_majuscule(lettre) :
    nb_converti = ord(lettre) #Convertit la lettre en chiffre
    if 'a' < nb_converti < 'z' : #Vérifie si c'est une minuscule
        nb_converti -= 32
    else :
        nb_converti += 32 
    print(chr(nb_converti)) #Reconvertit en lettre

invert_minuscule_majuscule('µ')
