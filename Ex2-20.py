volume = 0
input_vol = input("Commande :")
def vol () :
    global input_vol
    global volume
    while volume >= 0 and volume <= 100 :
        if input_vol == "+" :
            volume += 1
        elif input_vol == "-" :
            volume -= 1
        elif input_vol == "x" :
            print("Fermeture")
        else :
            input_vol = input("Commande :")

        print(volume)        

vol()
