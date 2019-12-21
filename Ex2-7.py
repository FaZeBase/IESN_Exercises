prix = int(input("Votre prix :"))
priorite = input("Nécéssaire, important, normal ?")

if priorite == "nécéssaire":
    print(prix * 1.06)
elif priorite == "important":
    print(prix * 1.12)
else :
    print(prix * 1.21)
